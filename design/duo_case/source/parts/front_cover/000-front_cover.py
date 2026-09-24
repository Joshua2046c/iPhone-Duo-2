w=param('front_cover_width',87.8)
h=param('front_cover_height',121.5)
t=param('front_cover_thickness',4.0)
r=param('front_cover_corner_radius',11.6)
depth=param('front_cover_storage_depth',2.6)
length=param('front_cover_storage_length',49.0)
height=param('front_cover_storage_height',85.4)
seat_l=param('front_cover_cap_seat_length',51.4)
seat_h=param('front_cover_cap_seat_height',90.6)
seat_depth=param('front_cover_cap_seat_depth',1.4)
pin_d=param('front_cover_pin_diameter',2.4)
pin_x=param('front_cover_pin_x',-18.9)
pin_y1=param('front_cover_pin_y1',-25.0)
pin_y2=param('front_cover_pin_y2',25.0)
pin_tip=param('front_cover_pin_tip',1.3)
outline=RectangleRounded(w,h,r)+Pos(-w/4,0)*Rectangle(w/2,h)
body=extrude(outline,amount=t)
for ll,hh,dd in ((seat_l,seat_h,seat_depth),(length,height,depth)):
 body-=Pos(-w/2+(ll-1)/2,0,(dd-1)/2)*Box(ll+1,hh,dd+1)
for yy in (pin_y1,pin_y2):
 body+=Pos(pin_x,yy,(pin_tip+depth+0.05)/2)*Cylinder(pin_d/2,depth+0.05-pin_tip)
assert t-depth>=1.4-1e-6
assert len(body.solids())==1
publish('front_cover',body,'04 前盖收纳腔')