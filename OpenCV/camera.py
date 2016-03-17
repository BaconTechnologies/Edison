import os
import subprocess
import cv2
import numpy as np
 
# Camera 0 is the integrated web cam on netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 retval, im = camera.read()
 return im
 
# Ramp the camera - these frames will be discarded and are only used to adjust light levels
for i in xrange(ramp_frames):
 temp = get_image()

print("Taking image...")

# Take the actual image we want to keep
camera_capture = get_image()
file = "plate.png"

# Save image
cv2.imwrite(file, camera_capture)
 
# Release camera
del(camera)

# Call openalpr software
apgtn = 'alpr -c mx plate.png'
subprocess.call(apgtn, shell=True)
