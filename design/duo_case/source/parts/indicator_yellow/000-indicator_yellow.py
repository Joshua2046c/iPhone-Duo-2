r=param('indicator_yellow_radius',1.8)
seat=param('indicator_yellow_seat_thickness',0.25)
body=Cylinder(r,seat,align=(Align.CENTER,Align.CENTER,Align.MIN))+Pos(0,0,seat)*Sphere(r,arc_size1=0,arc_size2=90,align=(Align.CENTER,Align.CENTER,Align.MIN))
assert len(body.solids())==1
body.color=Color(1.0,0.82,0.02)
publish('indicator_yellow',body,'09 黄色小球',material='petg')
