import time
import pyupm_grove as grove
import pyupm_ttp223 as ttp223

# Create button sensor in D8
button = grove.GroveButton(8)

# Create touch sensor in D4
touch = ttp223.TTP223(4)

# Read the input and print, waiting one second between readings
while 1:
	if button.value() :
		print 'Button Pressed!'
	else :
		print 'Button Not Pressed'

	if touch.value() :
		print 'Touch Pressed!'
	else :
		print 'Touch Not Pressed'
	time.sleep(1)

# Delete the button object
del button

# Delete the touch sensor object
del touch