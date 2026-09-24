# User image envelope. Internal contact plane retained at Z2.4.
PHONE_W, PHONE_H, HALF_T = 84.1, 117.8, 5.2
clearance = param('back_cover_fit_clearance', 0.25)
wall = param('back_cover_wall', 1.6)
plate = param('back_cover_plate', 3.4)
seat_z = param('back_cover_phone_seat_z', 2.4)
radius = param('back_cover_corner_radius', 10.0)
lip = param('back_cover_corner_inward', 0.4)
lip_h = param('back_cover_lip_height', 0.7)
corner_zone = param('back_cover_corner_zone', 15.0)
cam_w = param('back_cover_camera_width', 55.0)
cam_h = param('back_cover_camera_height', 23.0)
cam_x = param('back_cover_camera_x', 10.0)
cam_y = param('back_cover_camera_y', 42.5)
cam_land = param('back_cover_camera_ring_width', 2.0)
cam_clearance = param('back_cover_camera_ring_clearance', 0.2)
cam_depth = param('back_cover_camera_recess_depth', 0.4)
vol_x = param('back_cover_volume_x', 6.0)
vol_w = param('back_cover_volume_opening', 34.0)
power_y = param('back_cover_power_y', 18.0)
power_l = param('back_cover_power_opening', 21.0)
shutter_y = param('back_cover_shutter_y', -27.0)
shutter_l = param('back_cover_shutter_opening', 23.0)
bottom_w = param('back_cover_bottom_opening', 50.0)
channel_end = param('back_cover_channel_end_x', -12.7)
channel_y = param('back_cover_channel_center_y', -11.5)
channel_h = param('back_cover_channel_height', 75.0)
channel_depth = param('back_cover_channel_depth', 2.2)
seat_border = param('back_cover_seat_border', 2.0)
seat_depth = param('back_cover_seat_depth', 1.4)
pin_d = param('back_cover_pin_diameter', 2.4)
pin_x = param('back_cover_pin_x', -29.2)
pin_y1 = param('back_cover_pin_y1', -30.0)
pin_y2 = param('back_cover_pin_y2', 15.0)
pin_tip = param('back_cover_pin_tip_z', 1.3)
wi, hi = PHONE_W+2*clearance, PHONE_H+2*clearance
wo, ho = wi+2*wall, hi+2*wall
outside_z=seat_z-plate
outer = RectangleRounded(wo,ho,radius+wall)
inner = RectangleRounded(wi,hi,radius)
body = Pos(0,0,outside_z)*extrude(outer, amount=plate)
ring = extrude(outer,amount=HALF_T)-extrude(inner,amount=HALF_T)
ring -= Pos(-wo/2,0,HALF_T/2)*Box(2*wall+1, hi-2*corner_zone, HALF_T+2)
ring -= Pos(vol_x,ho/2,HALF_T/2)*Box(vol_w,2*wall+2,HALF_T+2)
ring -= Pos(wo/2,power_y,HALF_T/2)*Box(2*wall+2,power_l,HALF_T+2)
ring -= Pos(wo/2,shutter_y,HALF_T/2)*Box(2*wall+2,shutter_l,HALF_T+2)
ring -= Pos(0,-ho/2,HALF_T/2)*Box(bottom_w,2*wall+2,HALF_T+2)
body += Pos(0,0,seat_z)*ring
lip_ring = extrude(outer,amount=lip_h)-extrude(RectangleRounded(wi-2*lip,hi-2*lip,radius-lip),amount=lip_h)
for sx in (-1,1):
 for sy in (-1,1):
  zone=Pos(sx*(wo/2-corner_zone/2),sy*(ho/2-corner_zone/2),lip_h/2)*Box(corner_zone,corner_zone,lip_h+2)
  body += Pos(0,0,seat_z+HALF_T-lip_h)*(lip_ring & zone)
body -= Pos(cam_x,cam_y,outside_z-1)*extrude(SlotOverall(cam_w,cam_h),amount=plate+HALF_T+2)
body -= Pos(cam_x,cam_y,outside_z-1)*extrude(SlotOverall(cam_w+2*(cam_land+cam_clearance),cam_h+2*(cam_land+cam_clearance)),amount=1+cam_depth)
# Deep and shallow pockets face toward the phone. Camera ring recess faces outward.
start=-wo/2-0.2
seat_end=channel_end+seat_border
seat_floor=seat_z-seat_depth
channel_floor=seat_z-channel_depth
body -= Pos((start+seat_end)/2,channel_y,seat_floor+(seat_depth+1)/2)*Box(seat_end-start,channel_h+2*seat_border,seat_depth+1)
body -= Pos((start+channel_end)/2,channel_y,channel_floor+(channel_depth+1)/2)*Box(channel_end-start,channel_h,channel_depth+1)
for yy in (pin_y1,pin_y2):
 body += Pos(pin_x,yy,(channel_floor-0.05+pin_tip)/2)*Cylinder(pin_d/2,pin_tip-channel_floor+0.05)
assert plate-channel_depth >= 1.2-1e-6
assert channel_floor < pin_tip < seat_z
assert len(body.solids()) == 1
print('INNER channel floor',channel_floor,'outer back',outside_z,'residual floor',plate-channel_depth)
publish('back_cover',body,'01 弹性背盖')