from picamera2 import Picamera2, Preview
import time


picam2 = Picamera2()
picam2.resolution = (640, 480)
picture_name = input("filename: ")
picam2.exposure_mode = 'antishake'
config = picam2.create_preview_configuration(main= {"size": (806,606)}, controls = {"FrameDurationLimits":(40000, 40000)})
picam2.configure(config)
#picam2.start_preview(Preview.QTGL)
picam2.start_and_capture_file("/home/piai_C4/Desktop/%s"%picture_name)
picam2.stop()
print("Done")
