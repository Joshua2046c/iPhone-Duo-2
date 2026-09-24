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
# Model local bond face at Z0, with outward crest in -Z. Placement binds to recess.
base_z=phone_z-back_plate+recess-glue
crest_z=phone_z-cam_height-margin
thickness=base_z-crest_z
assert wall>=1.2 and thickness>=0.8 and margin>0
profile=SlotOverall(w+2*wall,h+2*wall)-SlotOverall(w,h)
body=extrude(profile,amount=-thickness)
assert len(body.solids())==1
print('Ring axial thickness',thickness,'crest world Z',crest_z,'assumed lens Z',phone_z-cam_height)
publish('camera_guard',body,'05 镜头保护圈')