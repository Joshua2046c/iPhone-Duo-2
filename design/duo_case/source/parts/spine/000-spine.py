# One developed sheet, two endpoint poses. Not a continuous phone hinge simulation.
import math
h=param('spine_height',84.0)
t=param('spine_thickness',0.6)
span=param('spine_bridge_span',11.9)
r=param('spine_bend_radius',1.6)
tail_l=param('spine_tail_length',30.0)
tab_l=param('spine_glue_tab_length',8.0)
slot_l=param('spine_slot_length',22.5)
slot_w=param('spine_slot_width',3.2)
slot_x=param('spine_slot_center_from_bend',17.0)
slot_y1=param('spine_slot_y1',-25.0)
slot_y2=param('spine_slot_y2',25.0)
flat=param('spine_flat_pose',False)
free_l=span+math.pi*r
if flat:
 # Bond end stays x>=0; every free millimetre extends left into the opened front.
 body=Pos((tab_l-free_l-tail_l)/2,0,-r)*Box(tab_l+free_l+tail_l,h,t)
 for yy in (slot_y1,slot_y2):
  body-=Pos(-free_l-slot_x,yy,-r-t)*extrude(SlotOverall(slot_l,slot_w),amount=3*t)
else:
 ri,ro=r-t/2,r+t/2
 body=Pos(-r,0,span/2)*Box(t,h,span)
 def elbow(zc,upper):
  annulus=Cylinder(ro,h,rotation=(90,0,0))-Cylinder(ri,h+2,rotation=(90,0,0))
  sign=1 if upper else -1
  return Pos(0,0,zc)*(annulus & (Pos(-ro/2,0,sign*ro/2)*Box(ro,h+2,ro)))
 body+=elbow(0,False)
 body+=Pos(tab_l/2,0,-r)*Box(tab_l,h,t)
 body+=elbow(span,True)
 body+=Pos(tail_l/2,0,span+r)*Box(tail_l,h,t)
 for yy in (slot_y1,slot_y2):
  body-=Pos(slot_x,yy,span+r-t)*extrude(SlotOverall(slot_l,slot_w),amount=3*t)
assert len(body.solids())==1
print('Developed free length:',free_l,'total:',free_l+tab_l+tail_l,'flat:',flat)
publish('spine',body,'02 前滑后粘护轴片')