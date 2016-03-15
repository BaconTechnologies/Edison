import time
import pyupm_grove as grove
import pyupm_ttp223 as ttp223

from internet import *

zoneNumber = "1"

# Create button sensor in D4
enterZone1 = grove.GroveButton(4)

# Create touch sensor in D3
exitZone1 = ttp223.TTP223(3)

# Initial configuration
init( zoneNumber )

# Read the input and print, waiting one second between readings
while 1:
	# Enter Zone detection
	if enterZone1.value() :
		enterZone()

	# Exit Zone detection
	if exitZone1.value() :
		exitZone()
	
	time.sleep(1)

# Delete the button object
del enterZone1

# Delete the touch sensor object
del exitZone1