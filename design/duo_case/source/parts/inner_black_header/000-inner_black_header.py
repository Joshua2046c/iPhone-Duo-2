w=param('inner_black_header_width',62)
h=param('inner_black_header_height',18)
t=param('inner_black_header_thickness',0.7)
r=param('inner_black_header_corner_radius',0.8)
body=extrude(RectangleRounded(w,h,r),amount=t)
assert len(body.solids())==1
body.color=Color(0.012,0.018,0.02)
publish('inner_black_header',body,'11 内侧黑色长块',material='petg')
