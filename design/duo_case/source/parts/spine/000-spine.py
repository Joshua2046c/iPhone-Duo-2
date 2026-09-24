from math import pi
h=param('spine_height',117.8)
t=param('spine_thickness',0.6)
span=param('spine_bridge_span',11.4)
r=param('spine_bend_radius',1.6)
tail_l=param('spine_tail_length',30.0)
tail_h=param('spine_tail_height',84.0)
tail_y=param('spine_tail_center_y',-15.0)
tab_l=param('spine_glue_tab_length',8.0)
tab_h=param('spine_glue_tab_height',104.0)
slot_l=param('spine_slot_length',21.5)
slot_w=param('spine_slot_width',3.2)
slot_x=param('spine_slot_center_from_bend',17.0)
slot_y1=param('spine_slot_y1',-35.0)
slot_y2=param('spine_slot_y2',12.0)
shoulder=param('spine_fullheight_shoulder_length',4.0)
flat=param('spine_flat_check',False)
inset=param('spine_flat_inset',0.5)
L=span+pi*r
# Local origin remains lower bend centre. Flat mode preserves neutral developed length.
if flat:
 shift=L+inset
 body=Pos(inset+L/2,0,-r)*Box(L,h,t)
 body+=Pos(inset-tab_l/2,0,-r)*Box(tab_l,tab_h,t)
 body+=Pos(shift+shoulder/2,0,-r)*Box(shoulder,h,t)
 body+=Pos(shift+tail_l/2,tail_y,-r)*Box(tail_l,tail_h,t)
else:
 shift=0
 ri,ro=r-t/2,r+t/2
 body=Pos(-r,0,span/2)*Box(t,h,span)
 def elbow(z,upper):
  ann=Cylinder(ro,h,rotation=(90,0,0))-Cylinder(ri,h+2,rotation=(90,0,0))
  return Pos(0,0,z)*(ann & (Pos(-ro/2,0,(1 if upper else -1)*ro/2)*Box(ro,h+2,ro)))
 body+=elbow(0,False)
 body+=elbow(span,True)
 body+=Pos(shoulder/2,0,-r)*Box(shoulder,h,t)
 body+=Pos(tail_l/2,tail_y,-r)*Box(tail_l,tail_h,t)
 body+=Pos(tab_l/2,0,span+r)*Box(tab_l,tab_h,t)
for yy in (slot_y1,slot_y2):
 body-=Pos(shift+slot_x,yy,-r-t)*extrude(SlotOverall(slot_l,slot_w),amount=3*t)
assert len(body.solids())==1
print('Developed free web',L,'storage shift',L+inset,'flat mode',flat)
publish('spine',body,'02 宽幅护轴片')