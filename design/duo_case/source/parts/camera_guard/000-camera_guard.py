# Custom ring. The camera protrusion is an explicit prototype assumption, not a vendor dimension.
w=param('camera_guard_inner_width',55.0)
h=param('camera_guard_inner_height',23.0)
wall=param('camera_guard_radial_width',2.0)
phone_z=param('camera_guard_phone_back_z',2.4)
back_plate=param('camera_guard_back_plate',3.4)
recess=param('camera_guard_recess_depth',0.4)
glue=param('camera_guard_glue_thickness',0.15)
cam_height=param('camera_guard_assumed_camera_protrusion',4.0)
margin=param('camera_guard_protection_margin',0.5)
end_r=param('camera_guard_outer_end_radius',11.75)
hinge_r=param('camera_guard_hinge_end_radius',10.8)
inner_depth=param('camera_guard_inner_cavity_depth',3.9)
extension=max(0.0,inner_depth-back_plate)
# Model local bond face at Z0, with outward crest in -Z. Placement binds to recess.
base_z=phone_z-back_plate-extension+recess-glue
crest_z=phone_z-cam_height-margin-extension
thickness=base_z-crest_z
assert wall>=1.2 and thickness>=0.8 and margin>0
# External tangents of two round glass ends give the slight photographed taper.
rr=end_r
rl=hinge_r
xr=w/2-rr
xl=-w/2+rl
nx=(rl-rr)/(xr-xl)
ny=(1-nx*nx)**0.5
tl=(xl+rl*nx,rl*ny)
tr=(xr+rr*nx,rr*ny)
glass=(Pos(xl,0)*Circle(rl)+Pos(xr,0)*Circle(rr)+
       Polygon(tl,(tl[0],-tl[1]),(tr[0],-tr[1]),tr,align=None))
profile=offset(glass,amount=wall)-glass
body=extrude(profile,amount=-thickness)
assert len(body.solids())==1
print('Ring axial thickness',thickness,'crest world Z',crest_z,'assumed lens Z',phone_z-cam_height)
publish('camera_guard',body,'05 镜头保护圈')
