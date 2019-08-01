import sys
import cv2
from djitellopy import Tello
import time

def main():
	print("Configuring tello Drone")
	tello = Tello()

	if not tello.connect():
		print("Tello not connected")
		return

	if not tello.streamon():
		print("Could not start video stream")
		return

	while(True):
		frame = tello.get_frame_read()
		cv2.imshow("DetectionResults", frame.frame)
		raw_key = cv2.waitKey(1)

		if raw_key == 27: #esc
			break

	cv2.destroyAllWindows()
	tello.end()

if __name__ == '__main__':
    sys.exit(main() or 0)
