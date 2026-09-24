# Installed curved pose. This is one continuous flexible sheet, NOT a rigid linkage simulation.
h = param('spine_height',117.8)
t = param('spine_thickness',0.6)
span = param('spine_bridge_span',11.5)
r = param('spine_bend_radius',1.6)
tail_l = param('spine_tail_length',18.5)
tail_h = param('spine_tail_height',73.0)
tail_y = param('spine_tail_center_y',-11.5)
tab_l = param('spine_glue_tab_length',8.0)
tab_h = param('spine_glue_tab_height',104.0)
slot_l = param('spine_slot_length',14.5)
slot_w = param('spine_slot_width',3.2)
slot_x = param('spine_slot_center_from_bend',9.25)
slot_y1 = param('spine_slot_y1',-30.0)
slot_y2 = param('spine_slot_y2',15.0)
# Local frame: lower bend centre (0,0,0), placed in assembly using cad.place.
ri,ro=r-t/2,r+t/2
body=Pos(-r,0,span/2)*Box(t,h,span)
def elbow(yc,width,zc,upper):
 annulus=(Cylinder(ro,width,rotation=(90,0,0))-Cylinder(ri,width+2,rotation=(90,0,0)))
 zsign=1 if upper else -1
 quadrant=Pos(-ro/2,0,zsign*ro/2)*Box(ro,width+2,ro)
 return Pos(0,yc,zc)*(annulus & quadrant)
body += elbow(tail_y,tail_h,0,False)
body += Pos(tail_l/2,tail_y,-r)*Box(tail_l,tail_h,t)
body += elbow(0,tab_h,span,True)
body += Pos(tab_l/2,0,span+r)*Box(tab_l,tab_h,t)
for yy in (slot_y1,slot_y2):
 body -= Pos(slot_x,yy,-r-t)*extrude(SlotOverall(slot_l,slot_w),amount=3*t)
assert slot_l > slot_w and tail_l > slot_l
assert len(body.solids()) == 1
print('Sheet span/thickness:',span,t,'slot:',slot_l,slot_w,'tail:',tail_l,tail_h)
publish('spine',body,'02 滑动护轴片')