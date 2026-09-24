# User-reference envelope; hinge-side short walls removed, top/bottom returns retained.
PHONE_W, PHONE_H, HALF_T = 84.1,117.8,5.2
clearance=param('back_cover_fit_clearance',0.25)
wall=param('back_cover_wall',1.6)
plate=param('back_cover_plate',3.4)
seat_z=param('back_cover_phone_seat_z',2.4)
radius=param('back_cover_corner_radius',10.0)
lip=param('back_cover_corner_inward',0.4)
lip_h=param('back_cover_lip_height',0.7)
corner_zone=param('back_cover_corner_zone',15.0)
trim=param('back_cover_hinge_edge_cut_width',2.2)
cam_w=param('back_cover_camera_width',55.0)
cam_h=param('back_cover_camera_height',23.0)
cam_x=param('back_cover_camera_x',10.0)
cam_y=param('back_cover_camera_y',42.5)
cam_land=param('back_cover_camera_ring_width',2.0)
cam_clearance=param('back_cover_camera_ring_clearance',0.2)
cam_depth=param('back_cover_camera_recess_depth',0.4)
vol_x=param('back_cover_volume_x',6.0)
vol_w=param('back_cover_volume_opening',34.0)
power_y=param('back_cover_power_y',18.0)
power_l=param('back_cover_power_opening',21.0)
shutter_y=param('back_cover_shutter_y',-27.0)
shutter_l=param('back_cover_shutter_opening',23.0)
bottom_w=param('back_cover_bottom_opening',50.0)
glue_l=param('back_cover_glue_recess_length',8.3)
glue_h=param('back_cover_glue_recess_height',115.0)
glue_depth=param('back_cover_glue_recess_depth',1.2)
corner_soft=param('back_cover_left_corner_radius',1.0)
opening_soft=param('back_cover_opening_edge_radius',0.3)
turn=param('back_cover_opening_turn_radius',1.0)
def outline(w,h,r):
 return RectangleRounded(w,h,r)+Pos(-w/4,0)*Rectangle(w/2,h)
wi,hi=PHONE_W+2*clearance,PHONE_H+2*clearance
wo,ho=wi+2*wall,hi+2*wall
outside_z=seat_z-plate
outer,inner=outline(wo,ho,radius+wall),outline(wi,hi,radius)
left_vertices=[v for v in outer.vertices() if abs(v.X+wo/2)<1e-6]
assert len(left_vertices)==2
outer=fillet(left_vertices,radius=corner_soft)
body=Pos(0,0,outside_z)*extrude(outer,amount=plate)
ring=extrude(outer,amount=HALF_T)-extrude(inner,amount=HALF_T)
# The continuous hinge-side cut removes both former corner wall stubs, not the back plate.
ring-=Pos(-wo/2+(trim-1)/2,0,HALF_T/2)*Box(trim+1,ho+2,HALF_T+2)
ring-=Pos(vol_x,ho/2,HALF_T/2)*Box(vol_w+2*turn,2*wall+2,HALF_T+2)
ring-=Pos(wo/2,power_y,HALF_T/2)*Box(2*wall+2,power_l+2*turn,HALF_T+2)
ring-=Pos(wo/2,shutter_y,HALF_T/2)*Box(2*wall+2,shutter_l+2*turn,HALF_T+2)
ring-=Pos(0,-ho/2,HALF_T/2)*Box(bottom_w+2*turn,2*wall+2,HALF_T+2)
body+=Pos(0,0,seat_z)*ring
lip_ring=extrude(outer,amount=lip_h)-extrude(outline(wi-2*lip,hi-2*lip,radius-lip),amount=lip_h)
lip_ring-=Pos(-wo/2+(trim-1)/2,0,lip_h/2)*Box(trim+1,ho+2,lip_h+2)
for sx in (-1,1):
 for sy in (-1,1):
  zone=Pos(sx*(wo/2-corner_zone/2),sy*(ho/2-corner_zone/2),lip_h/2)*Box(corner_zone,corner_zone,lip_h+2)
  body+=Pos(0,0,seat_z+HALF_T-lip_h)*(lip_ring&zone)
body-=Pos(cam_x,cam_y,outside_z-1)*extrude(SlotOverall(cam_w,cam_h),amount=plate+HALF_T+2)
body-=Pos(cam_x,cam_y,outside_z-1)*extrude(SlotOverall(cam_w+2*(cam_land+cam_clearance),cam_h+2*(cam_land+cam_clearance)),amount=1+cam_depth)
body-=Pos(-wo/2+(glue_l-1)/2,0,seat_z-glue_depth+(glue_depth+1)/2)*Box(glue_l+1,glue_h,glue_depth+1)

# Profile blends are independent of the small through-thickness edge roll.
# Widen by one turn radius at each end so the original rectangular access remains clear.
eps=1e-5
openings=(
 ('y',ho/2,hi/2,vol_x-vol_w/2-turn,vol_x+vol_w/2+turn),
 ('y',-ho/2,-hi/2,-bottom_w/2-turn,bottom_w/2+turn),
 ('x',wo/2,wi/2,power_y-power_l/2-turn,power_y+power_l/2+turn),
 ('x',wo/2,wi/2,shutter_y-shutter_l/2-turn,shutter_y+shutter_l/2+turn))
turn_edges=[]
for axis,outer_side,inner_side,lo,upper in openings:
 chosen=[]
 for e in body.edges():
  if e.geom_type!=GeomType.LINE:
   continue
  bb=e.bounding_box()
  amin,amax=(bb.min.X,bb.max.X) if axis=='x' else (bb.min.Y,bb.max.Y)
  bmin,bmax=(bb.min.Y,bb.max.Y) if axis=='x' else (bb.min.X,bb.max.X)
  at_end=(abs(bmin-lo)<eps and abs(bmax-lo)<eps) or (abs(bmin-upper)<eps and abs(bmax-upper)<eps)
  level=abs(bb.max.Z-bb.min.Z)<eps and (abs(bb.min.Z-seat_z)<eps or abs(bb.min.Z-seat_z-HALF_T)<eps)
  through_wall=amin>=min(outer_side,inner_side)-eps and amax<=max(outer_side,inner_side)+eps and amax-amin>eps
  if at_end and level and through_wall:
   chosen.append(e)
 assert len(chosen)==4, 'Expected two lower and two upper profile corners'
 turn_edges.extend(chosen)
body=fillet(turn_edges,radius=turn)

# Roll the touch-facing outer U rim, including its new profile arcs.
opening_edges=[]
for axis,outer_side,inner_side,lo,upper in openings:
 chosen=[]
 for e in body.edges():
  bb=e.bounding_box()
  amin,amax=(bb.min.X,bb.max.X) if axis=='x' else (bb.min.Y,bb.max.Y)
  bmin,bmax=(bb.min.Y,bb.max.Y) if axis=='x' else (bb.min.X,bb.max.X)
  on_outer=abs(amin-outer_side)<eps and abs(amax-outer_side)<eps
  on_inner=abs(amin-inner_side)<eps and abs(amax-inner_side)<eps
  in_span=bmin>=lo-turn-eps and bmax<=upper+turn+eps
  rising=bb.max.Z-bb.min.Z>eps
  if bb.min.Z>=seat_z-eps and in_span and on_outer:
   chosen.append(e)
 assert len(chosen)>=5, 'Incomplete blended rim'
 opening_edges.extend(chosen)
body=fillet(opening_edges,radius=opening_soft)
for axis,outer_side,inner_side,lo,upper in openings:
 center=(lo+upper)/2
 span=upper-lo-2*turn
 if axis=='x':
  access=Pos(outer_side,center,seat_z+HALF_T/2)*Box(2*wall+2,span,HALF_T)
 else:
  access=Pos(center,outer_side,seat_z+HALF_T/2)*Box(span,2*wall+2,HALF_T)
 assert (body & access).volume<1e-6, 'Original rectangular button passage obstructed'

assert plate-glue_depth>=1.2
assert len(body.solids())==1
publish('back_cover',body,'01 开边胶接背盖')