w=param('front_cover_width',87.8)
h=param('front_cover_height',121.5)
t=param('front_cover_thickness',2.2)
r=param('front_cover_corner_radius',11.6)
groove_end=param('front_cover_groove_end_x',-35.4)
groove_height=param('front_cover_groove_height',104.6)
groove_y=param('front_cover_groove_y',0.0)
groove_depth=param('front_cover_groove_depth',1.0)
flush_y=param('front_cover_hinge_end_halfheight',58.9)
flush_x=param('front_cover_hinge_end_trim_x',50.0)
hinge_x=param('front_cover_hinge_edge_x',-43.7)
tuck=param('front_cover_tuck_edge_relief',1.1)
ledge=param('front_cover_tuck_edge_thickness',0.8)
body=extrude(RectangleRounded(w,h,r),amount=t)
for sy in (-1,1):
 body-=Pos(flush_x-50,sy*(flush_y+10),t/2)*Box(100,20,t+2)
body-=Pos(hinge_x-5,0,t/2)*Box(10,h+2,t+2)
start=-w/2-1
body-=Pos((start+groove_end)/2,groove_y,(groove_depth-1)/2)*Box(groove_end-start,groove_height,groove_depth+1)
# Heel relief preserves the bond land but clears the back pocket floor in the flat capacity pose.
body-=Pos((start+hinge_x+tuck)/2,0,ledge+(t-ledge+1)/2)*Box(hinge_x+tuck-start,h+2,t-ledge+1)
assert len(body.solids())==1
assert hinge_x+tuck < -84.1/2 # user reference phone half-width
publish('front_cover',body,'04 齐平前盖')