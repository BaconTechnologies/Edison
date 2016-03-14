import time
import pyupm_grove as grove
import pyupm_ttp223 as ttp223

from internet import *

# Create button sensor in D8
button = grove.GroveButton(8)

# Create touch sensor in D4
touch = ttp223.TTP223(4)

# Read the input and print, waiting one second between readings
whereAreYouGoing = "2"
while 1:
	if button.value() :
		whereAreYouGoing = "1"
		request( whereAreYouGoing )
	else :
		print 'Button Not Pressed'

	if touch.value() :
		whereAreYouGoing = "2"
		request( whereAreYouGoing )
	else :
		print 'Touch Not Pressed'
	
	time.sleep(2)

# Delete the button object
del button

# Delete the touch sensor object
del touch