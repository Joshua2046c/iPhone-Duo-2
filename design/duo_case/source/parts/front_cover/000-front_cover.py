w=param('front_cover_width',87.8)
h=param('front_cover_height',121.5)
t=param('front_cover_thickness',2.2)
r=param('front_cover_corner_radius',11.6)
groove_end=param('front_cover_groove_end_x',-35.4)
groove_height=param('front_cover_groove_height',104.6)
groove_y=param('front_cover_groove_y',0.0)
groove_depth=param('front_cover_groove_depth',1.0)
# Solid full-face lid. Only the left-edge adhesive recess is cut into its underside.
body=extrude(RectangleRounded(w,h,r),amount=t)
start=-w/2-1
body -= Pos((start+groove_end)/2,groove_y,(groove_depth-1)/2)*Box(groove_end-start,groove_height,groove_depth+1)
assert t-groove_depth>=1.2-1e-6
assert len(body.solids())==1
publish('front_cover',body,'04 完整前盖')