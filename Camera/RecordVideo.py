from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
picam2.resolution = (640, 480)
picam2.framerate = 30
record_duration = int(input("duration time in sec: "))
video_name = input("filename: ")
picam2.exposure_mode = 'antishake'
config = picam2.create_preview_configuration(main= {"size": (806,606)}, controls = {"FrameDurationLimits":(40000, 40000)})
picam2.configure(config)
#picam2.start_preview(Preview.QTGL)
picam2.start_and_record_video("/home/piai_C4/Desktop/%s"%video_name, duration=record_duration+1)
picam2.stop()
print("Done")
