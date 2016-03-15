import time
import pyupm_grove as grove
import pyupm_ttp223 as ttp223

from internet import *

zoneNumber = "2"

# Create button sensor in D8
enterZone2 = grove.GroveButton(8)

# Create touch sensor in D7
exitZone2 = ttp223.TTP223(7)

# Read the input and print, waiting one second between readings
while 1:
	if enterZone2.value() :
		enterZone( zoneNumber )
	
	if exitZone2.value() :
		exitZone( zoneNumber )
	
	time.sleep(1)

# Delete the button object
del enterZone2

# Delete the touch sensor object
del exitZone2