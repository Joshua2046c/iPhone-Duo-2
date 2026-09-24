w=param('retainer_width',33.1)
h=param('retainer_height',78.6)
t=param('retainer_thickness',1.0)
relief=param('retainer_roof_relief',0.2)
end_land=param('retainer_end_bond_land',2.3)
side_land=param('retainer_side_bond_land',2.1)
# Local origin is the centre of the lower face. Three raised glue lands, open left mouth.
skin=param('retainer_decor_skin',0.2)
body=Pos(0,0,(t-skin)/2)*Box(w,h,t+skin)
cut_left=-w/2-1
cut_right=w/2-end_land
body -= Pos((cut_left+cut_right)/2,0,t-relief/2+0.5)*Box(cut_right-cut_left,h-2*side_land,relief+1)

# Coordinate interface from the current closed assembly:
# retainer object placement is X=-18.3; front placement is X=0.
# Added skin makes the two visible inner surfaces coplanar, without moving rail faces.
FRONT_TO_RETAINER_X=18.3
seat_depth=param('retainer_decor_recess_depth',0.15)
seat_gap=param('retainer_decor_seat_clearance',0.15)
long_w=param('retainer_inner_long_width',62.0)
black_h=param('retainer_inner_black_height',18.0)
blue_h=param('retainer_inner_blue_height',20.0)
top_y=param('retainer_inner_top_y',31.0)
blue_y=param('retainer_inner_blue_y',8.0)
corner=param('retainer_inner_corner_radius',0.8)
bar_l=param('retainer_inner_bar_length',10.0)
bar_w=param('retainer_inner_bar_width',1.6)
bar_first_u=param('retainer_inner_bar_first_u',15.0)
bar_pitch=param('retainer_inner_bar_pitch',11.0)
bar_y=param('retainer_inner_bar_y',-6.0)
disk_d=param('retainer_inner_disk_diameter',7.0)
disk_u=param('retainer_inner_disk_u',25.0)
disk_y=param('retainer_inner_disk_y',-23.0)
lower_w=param('retainer_inner_lower_width',24.0)
lower_h=param('retainer_inner_lower_height',10.0)
lower_u=param('retainer_inner_lower_u',20.0)
lower_y=param('retainer_inner_lower_y',-40.0)
def inner_cut(sk,u,y):
 return Pos(FRONT_TO_RETAINER_X-u,y,-skin-0.1)*extrude(sk,amount=seat_depth+0.1)
for uu,yy,ww,hh in ((0,top_y,long_w,black_h),(0,blue_y,long_w,blue_h),
                     (lower_u,lower_y,lower_w,lower_h)):
 body-=inner_cut(RectangleRounded(ww+2*seat_gap,hh+2*seat_gap,corner+seat_gap),uu,yy)
for i in range(2):
 body-=inner_cut(SlotOverall(bar_l+2*seat_gap,bar_w+2*seat_gap),bar_first_u+i*bar_pitch,bar_y)
body-=inner_cut(Circle(disk_d/2+seat_gap),disk_u,disk_y)
assert t+skin-relief-seat_depth>=0.8-1e-6
print('Retainer remaining below decoration recess:',t+skin-relief-seat_depth)
body.color=Color(0.80,0.015,0.055)

assert len(body.solids())==1
assert t-relief>=0.8
publish('retainer',body,'03 内侧装饰盖板',material='petg')