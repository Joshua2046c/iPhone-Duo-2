w=param('inner_blue_grid_width',62)
h=param('inner_blue_grid_height',20)
t=param('inner_blue_grid_thickness',0.7)
r=param('inner_blue_grid_corner_radius',0.8)
body=extrude(RectangleRounded(w,h,r),amount=t)
groove_w=param('inner_blue_grid_groove_width',0.5)
groove_d=param('inner_blue_grid_groove_depth',0.25)
# User reference specifies two rows of five cells, ten total.
for i in range(1,5):
 body-=Pos(-w/2+i*w/5,0,t-groove_d)*extrude(Rectangle(groove_w,h+0.2),amount=groove_d+0.1)
body-=Pos(0,0,t-groove_d)*extrude(Rectangle(w+0.2,groove_w),amount=groove_d+0.1)
assert t-groove_d>=0.4
assert len(body.solids())==1
body.color=Color(0.015,0.48,0.92)
publish('inner_blue_grid',body,'12 两排十格蓝块',material='petg')
