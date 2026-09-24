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
def outline(w,h,r):
 return RectangleRounded(w,h,r)+Pos(-w/4,0)*Rectangle(w/2,h)
wi,hi=PHONE_W+2*clearance,PHONE_H+2*clearance
wo,ho=wi+2*wall,hi+2*wall
outside_z=seat_z-plate
outer,inner=outline(wo,ho,radius+wall),outline(wi,hi,radius)
body=Pos(0,0,outside_z)*extrude(outer,amount=plate)
ring=extrude(outer,amount=HALF_T)-extrude(inner,amount=HALF_T)
# The continuous hinge-side cut removes both former corner wall stubs, not the back plate.
ring-=Pos(-wo/2+(trim-1)/2,0,HALF_T/2)*Box(trim+1,ho+2,HALF_T+2)
ring-=Pos(vol_x,ho/2,HALF_T/2)*Box(vol_w,2*wall+2,HALF_T+2)
ring-=Pos(wo/2,power_y,HALF_T/2)*Box(2*wall+2,power_l,HALF_T+2)
ring-=Pos(wo/2,shutter_y,HALF_T/2)*Box(2*wall+2,shutter_l,HALF_T+2)
ring-=Pos(0,-ho/2,HALF_T/2)*Box(bottom_w,2*wall+2,HALF_T+2)
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
assert plate-glue_depth>=1.2
assert len(body.solids())==1
publish('back_cover',body,'01 开边胶接背盖')