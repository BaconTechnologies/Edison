import time
import pyupm_grove as grove

# Create the button object using GPIO pin 0
button = grove.GroveButton(8)

# Read the input and print, waiting one second between readings
while 1:
	if button.value() :
		print 'Pressed!'
	else :
		print 'Not Pressed'
	time.sleep(1)

# Delete the button object
del button