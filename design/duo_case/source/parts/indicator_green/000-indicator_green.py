r=param('indicator_green_radius',1.8)
seat=param('indicator_green_seat_thickness',0.25)
body=Cylinder(r,seat,align=(Align.CENTER,Align.CENTER,Align.MIN))+Pos(0,0,seat)*Sphere(r,arc_size1=0,arc_size2=90,align=(Align.CENTER,Align.CENTER,Align.MIN))
assert len(body.solids())==1
body.color=Color(0.015,0.7,0.15)
publish('indicator_green',body,'10 绿色小球',material='petg')
