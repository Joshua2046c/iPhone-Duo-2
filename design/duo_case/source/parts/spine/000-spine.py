# cell: spine
# One developed sheet, two endpoint poses. Not a continuous phone hinge simulation.
import math
h=param('spine_height',84.0)
t=param('spine_thickness',0.76)
tail_h=param('spine_sliding_tail_height',115.3)
assert 0<tail_h<=h
span=param('spine_bridge_span',11.9)
r=param('spine_bend_radius',1.6)
tail_l=param('spine_tail_length',30.0)
tab_l=param('spine_glue_tab_length',8.0)
slot_l=param('spine_slot_length',22.5)
slot_w=param('spine_slot_width',3.2)
slot_r=param('spine_slot_corner_radius',2.1)
assert 0<2*slot_r<min(slot_l,slot_w)
slot_profile=RectangleRounded(slot_l,slot_w,slot_r)
assert abs(slot_profile.area-(slot_l*slot_w-(4-math.pi)*slot_r**2))<1e-5
slot_x=param('spine_slot_center_from_bend',17.0)
slot_y1=param('spine_slot_y1',-25.0)
slot_y2=param('spine_slot_y2',25.0)
flat=param('spine_flat_pose',False)
free_l=span+math.pi*r
# Keep the original material datum; the developed underside remains on world Z0.
tip_r=param('spine_tail_corner_radius',3.0)
REFERENCE_THICKNESS=0.15
R=r+REFERENCE_THICKNESS/2
z0=-R
A=math.pi*r/2
end_s=free_l+tail_l
assert 0<t<R
assert abs(h-tail_h)<1e-6, 'Uniform sheet uses the same full and tail height'
def point(x,z):
 return (x,-h/2,z)
def flat_p(ss,top=False):
 return point(-ss,z0+(t if top else 0))
def tail_p(ss,top=False):
 return point(ss-free_l,span+R-(t if top else 0))
def lower_p(ss,rr):
 angle=ss/r
 return point(-rr*math.sin(angle),-rr*math.cos(angle))
def upper_p(angle,rr):
 return point(-rr*math.cos(angle),span+rr*math.sin(angle))

if flat:
 edges=[Line(flat_p(-tab_l),flat_p(end_s)),
        Line(flat_p(end_s),flat_p(end_s,True)),
        Line(flat_p(end_s,True),flat_p(-tab_l,True)),
        Line(flat_p(-tab_l,True),flat_p(-tab_l))]
else:
 # Constant-thickness material follows the same closed reference path.
 edges=[Line(point(tab_l,-R),point(0,-R)),
        ThreePointArc(lower_p(0,R),lower_p(A/2,R),lower_p(A,R)),
        Line(point(-R,0),point(-R,span)),
        ThreePointArc(upper_p(0,R),upper_p(math.pi/4,R),upper_p(math.pi/2,R)),
        Line(tail_p(free_l),tail_p(end_s)),
        Line(tail_p(end_s),tail_p(end_s,True)),
        Line(tail_p(end_s,True),tail_p(free_l,True)),
        ThreePointArc(upper_p(math.pi/2,R-t),upper_p(math.pi/4,R-t),upper_p(0,R-t)),
        Line(point(-R+t,span),point(-R+t,0)),
        ThreePointArc(lower_p(A,R-t),lower_p(A/2,R-t),lower_p(0,R-t)),
        Line(point(0,-R+t),point(tab_l,-R+t)),
        Line(point(tab_l,-R+t),point(tab_l,-R))]
section=Face(Wire([edge for curve in edges for edge in curve.edges()]))
body=extrude(section,amount=h,dir=(0,1,0))
assert len(body.solids())==1
# Round only the two free-tail outer corners of the uniform sheet.
tip_x=-end_s if flat else tail_l
corner_edges=[]
for edge in body.edges():
 bb=edge.bounding_box()
 if abs(bb.size.Z-t)<1e-6 and bb.size.X<1e-6 and bb.size.Y<1e-6 and abs(bb.min.X-tip_x)<1e-6 and abs(abs(bb.min.Y)-tail_h/2)<1e-6:
  corner_edges.append(edge)
assert len(corner_edges)==2
prior_volume=body.volume
body=fillet(corner_edges,radius=tip_r)
if flat:
 assert abs(prior_volume-body.volume-2*(1-math.pi/4)*tip_r**2*t)<1e-4
# Exact developed corner volume is checked above; curved spline-face mass integration is approximate.
for yy in (slot_y1,slot_y2):
 if flat:
  body-=Pos(-free_l-slot_x,yy,z0-1)*extrude(slot_profile,amount=t+2)
 else:
  body-=Pos(slot_x,yy,span-R-1)*extrude(slot_profile,amount=2*R+2)
  slot_min=slot_x-slot_l/2
  if slot_min<0:
   assert slot_min+slot_r<=-A and slot_min>=-A-span
   body-=Pos(-R/2,yy,span+R/2)*Box(R+0.02,slot_w,R+0.02)
   body-=Pos(-R+2*t,yy,span+A+slot_x)*Rot(0,-90,0)*extrude(slot_profile,amount=4*t)
assert len(body.solids())==1
if flat:
 assert abs(body.bounding_box().min.Z-z0)<1e-6
 for ss in (0,2,12,22.36,end_s-5):
  expected=t
  probe=body & Pos(-ss,0,z0+t/2)*Box(0.01,0.01,t+2)
  assert abs(probe.bounding_box().size.Z-expected)<1e-6, 'Plateau thickness differs'
print('Uniform sheet thickness',t,'flat bottom',z0,'flat top',z0+t,'no recessed band')
print('Slots unchanged',slot_l,slot_w,'corner R',slot_r,'center from bend',slot_x,'Y',slot_y1,slot_y2)
print('Developed free length',free_l,'total',end_s+tab_l,'flat',flat)
publish('spine',body,'02 前滑后粘护轴片',material='tpu')
