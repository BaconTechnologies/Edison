import os
import subprocess
import cv2
import numpy as np
import urllib2
import json
 
# Camera 0 is the integrated web cam on netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(0)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 retval, im = camera.read()
 return im
 
# Ramp the camera - these frames will be discarded and are only used to adjust light levels
for i in xrange(ramp_frames):
 temp = get_image()

# Take the actual image we want to keep
camera_capture = get_image()
file = "plate.png"

# Save image
cv2.imwrite(file, camera_capture)
 
# Release camera
del(camera)

# Call openalpr software
apgtn = 'alpr -c mx plate.png > data.txt'
subprocess.call(apgtn, shell=True)


flag = False;
with open("data.txt") as f:
    for line in f:
	if line == "No license plates found.\n":
		print "error"
		break
	else:
		if flag:
			arr = line.split(' ')
			print arr[len(arr)-3]
			#JSON magic
			
			break
		else:
			flag = True

