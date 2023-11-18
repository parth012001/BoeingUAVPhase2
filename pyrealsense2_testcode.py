import pyrealsense2 as rs
import numpy as np

pipe = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

pipe.start(config)

try:
	while True:
		frames = pipe.wait_for_frames()
		depth_frame = frames.get_depth_frame()

		if not depth_frame:
			continue
		
		depth_image = np.asanyarray(depth_frame.get_data())

		height, width = depth_image.shape
		center_x, center_y = width//2, height//2
		depth = depth_image[center_y, center_x]

		depth_meters = depth/1000.0

		print(f'Dist to center obj: {depth_meters}m')
except KeyboardInterrupt:
	pass
finally:
	pipe.stop()
