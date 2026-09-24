w=param('retainer_width',33.1)
h=param('retainer_height',78.6)
t=param('retainer_thickness',1.0)
relief=param('retainer_roof_relief',0.2)
end_land=param('retainer_end_bond_land',2.3)
side_land=param('retainer_side_bond_land',2.1)
# Local origin is the centre of the lower face. Three raised glue lands, open left mouth.
body=Pos(0,0,t/2)*Box(w,h,t)
cut_left=-w/2-1
cut_right=w/2-end_land
body -= Pos((cut_left+cut_right)/2,0,t-relief/2+0.5)*Box(cut_right-cut_left,h-2*side_land,relief+1)
assert len(body.solids())==1
assert t-relief>=0.8
publish('retainer',body,'03 滑动压盖')