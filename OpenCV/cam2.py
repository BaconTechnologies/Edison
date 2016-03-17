import cv2
import time

camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
def get_image():
 retval, im = camera.read()
 return im

for i in xrange(ramp_frames):
 temp = get_image()
mon = 1
while mon <2:
     print("Taking image...")
     camera_capture = get_image()
     file = "/home/root/Edison/OpenCV/"+str(mon)+".png"
     cv2.imwrite(file, camera_capture)
     time.sleep(0.1)
     mon+=1
del(camera)