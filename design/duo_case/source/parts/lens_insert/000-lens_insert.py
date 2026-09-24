# One integrated two-colour insert. Colour regions share a full face,
# with no assembly clearance; print together as one multi-colour part.
d=param('lens_insert_base_diameter',18.0)
t=param('lens_insert_base_thickness',1.0)
r=param('lens_insert_hemisphere_radius',7.0)
base=Cylinder(d/2,t,align=(Align.CENTER,Align.CENTER,Align.MIN))
dome=Pos(0,0,t)*Sphere(r,arc_size1=0,arc_size2=90,align=(Align.CENTER,Align.CENTER,Align.MIN))
assert len((base+dome).solids())==1
base.label='White base'
base.color=Color(0.97,0.97,0.95)
dome.label='Blue hemisphere'
dome.color=Color(0.015,0.48,0.92)
body=Compound(children=[base,dome])
publish('lens_insert',body,'06 蓝白一体双色嵌件',material='petg')
