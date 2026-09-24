# Front cover and its coordinated decorative pocket interfaces.
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
seat_r=param('front_cover_cap_seat_radius',10.35)
seat_left_r=param('front_cover_cap_seat_left_radius',0.8)
bond_gap=param('front_cover_cap_bond_gap',0.2)
pin_d=param('front_cover_pin_diameter',2.4)
pin_x=param('front_cover_pin_x',-18.9)
pin_y1=param('front_cover_pin_y1',-25.0)
pin_y2=param('front_cover_pin_y2',25.0)
pin_tip=param('front_cover_pin_tip',1.3)

# All outer decorations share this shallow adhesive seating interface.
recess=param('front_cover_decor_recess_depth',0.2)
clearance=param('front_cover_decor_edge_clearance',0.15)
lens_d=param('front_cover_lens_seat_diameter',18.0)
lens_x=param('front_cover_lens_seat_x',-29.0)
lens_y=param('front_cover_lens_seat_y',44.0)
balls_d=param('front_cover_ball_seat_diameter',3.6)
balls_x=param('front_cover_ball_first_x',-10.0)
balls_y=param('front_cover_ball_row_y',49.2)
balls_pitch=param('front_cover_ball_pitch',7.0)
arrow_w=param('front_cover_arrow_width',7.0)
arrow_h=param('front_cover_arrow_height',9.0)
arrow_x=param('front_cover_arrow_x',34.0)
arrow_y=param('front_cover_arrow_y',0.0)
slot_l=param('front_cover_lower_slot_length',34.0)
slot_w=param('front_cover_lower_slot_width',2.4)
slot_x=param('front_cover_lower_slot_x',0.0)
slot_y=param('front_cover_lower_slot_y',-44.0)

corner_soft=param('front_cover_left_corner_radius',1.0)
outline=RectangleRounded(w,h,r)+Pos(-w/4,0)*Rectangle(w/2,h)
left_vertices=[v for v in outline.vertices() if abs(v.X+w/2)<1e-6]
assert len(left_vertices)==2
outline=fillet(left_vertices,radius=corner_soft)
body=extrude(outline,amount=t)
# Full inset cover seat, matching the asymmetrical outline.
seat=RectangleRounded(seat_l,seat_h,seat_r)+Pos(-seat_l/4,0)*Rectangle(seat_l/2,seat_h)
seat=fillet([v for v in seat.vertices() if abs(v.X+seat_l/2)<1e-6],radius=seat_left_r)
body-=Pos(0,0,-0.1)*extrude(seat,amount=seat_depth+0.1)
# Recess stays open at the hinge only at the sheet's sliding height.
mouth_floor=seat_depth-bond_gap
body-=Pos(-w/2+(length-1)/2,0,(mouth_floor+depth)/2)*Box(length+1,height,depth-mouth_floor)
for yy in (pin_y1,pin_y2):
 body+=Pos(pin_x,yy,(pin_tip+depth+0.05)/2)*Cylinder(pin_d/2,depth+0.05-pin_tip)
def pocket(sketch,x,y):
 return Pos(x,y,t-recess)*extrude(sketch,amount=recess+0.1)
body-=pocket(Circle(lens_d/2+clearance),lens_x,lens_y)
for i in range(3):
 body-=pocket(Circle(balls_d/2+clearance),balls_x+i*balls_pitch,balls_y)
tri=Polygon((-arrow_w/2,0),(arrow_w/2,-arrow_h/2),(arrow_w/2,arrow_h/2),align=None)
body-=pocket(offset(tri,amount=clearance),arrow_x,arrow_y)
body-=pocket(SlotOverall(slot_l,slot_w),slot_x,slot_y)

assert t-depth-recess>=1.2-1e-6
assert len(body.solids())==1
body.color=Color(0.80,0.015,0.055)
publish('front_cover',body,'04 整面台阶前盖',material='petg')
