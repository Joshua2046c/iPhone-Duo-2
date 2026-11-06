w=param('retainer_width',33.1)
h=param('retainer_height',78.6)
t=param('retainer_thickness',1.0)
relief=param('retainer_roof_relief',0.2)
end_land=param('retainer_end_bond_land',2.3)
side_land=param('retainer_side_bond_land',2.1)
rail_y=param('retainer_rail_relief_y',13.7)
# Centred full cover with asymmetrical shell outline and an open hinge-side rail relief.
skin=param('retainer_decor_skin',0.2)
corner_r=param('retainer_corner_radius',10.15)
left_r=param('retainer_left_corner_radius',0.6)
outline=RectangleRounded(w,h,corner_r)+Pos(-w/4,0)*Rectangle(w/2,h)
outline=fillet([v for v in outline.vertices() if abs(v.X+w/2)<1e-6],radius=left_r)
body=Pos(0,0,-skin)*extrude(outline,amount=t+skin)
cut_left=-w/2-1
cut_right=w/2-end_land
if relief>0:
 body -= Pos((cut_left+cut_right)/2,rail_y,t-relief/2+0.5)*Box(cut_right-cut_left,h-2*side_land,relief+1)

# Retainer is centred on the shortened outline; artwork stays in the fixed assembly datum.
front_offset=param('retainer_front_x_offset',1.55)
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
white_w=param('retainer_inner_white_width',24.0)
white_h=param('retainer_inner_white_height',9.0)
white_u=param('retainer_inner_white_u',-20.0)
white_y=param('retainer_inner_white_y',-18.0)
def inner_cut(sk,u,y):
 return Pos(-u-front_offset,y,-skin-0.1)*extrude(sk,amount=seat_depth+0.1)
for uu,yy,ww,hh in ((0,blue_y,long_w,blue_h),
                     (white_u,white_y,white_w,white_h)):
 body-=inner_cut(RectangleRounded(ww+2*seat_gap,hh+2*seat_gap,corner+seat_gap),uu,yy)
body-=inner_cut(Circle(disk_d/2+seat_gap),disk_u,disk_y)
# Five marked motifs are raised material in the same plate, without insert pockets.
raised=param('retainer_integral_decor_height',0.6)
assert raised>0
integral_profiles=[(0,top_y,RectangleRounded(long_w,black_h,corner))]
for i in range(2):
 integral_profiles.append((bar_first_u+i*bar_pitch,bar_y,SlotOverall(bar_l,bar_w)))
for uu in (lower_u,-lower_u):
 integral_profiles.append((uu,lower_y,RectangleRounded(lower_w,lower_h,corner)))
for uu,yy,profile in integral_profiles:
 feature=Pos(-uu-front_offset,yy,-skin)*extrude(profile,amount=-raised)
 body+=feature
 assert len(body.solids())==1, 'Raised motif must fuse to the plate'
print('Integral motifs',len(integral_profiles),'protrusion',raised,'top local Z',-skin-raised)
assert len(integral_profiles)==5
# A zero relief makes the marked panel flush with the right hand seating surface.
remaining=t+skin-relief-seat_depth
assert remaining>1e-6, 'Relief breaks through a decorative pocket'
assert 0<side_land<h/2 and 0<=relief<t+skin
print('Retainer remaining below decoration recess:',remaining)
print('Relief depth',relief,'floor local Z',t-relief,'end borders',side_land,'relief Y length',h-2*side_land)
body.color=Color(0.80,0.015,0.055)

assert len(body.solids())==1
assert t+skin-relief>0, 'Relief breaks through cover skin'
publish('retainer',body,'03 一体内侧装饰盖板',material='petg')
