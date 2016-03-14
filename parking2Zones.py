import time
import pyupm_grove as grove
import pyupm_ttp223 as ttp223

import pyupm_i2clcd as lcd

from internet import *

# Create button sensor in D8 && D4
enterZone1 = grove.GroveButton(4)
enterZone2 = grove.GroveButton(8)

# Create touch sensor in D7 && D3
exitZone1 = ttp223.TTP223(3)
exitZone2 = ttp223.TTP223(7)

# Initialize LCD Displays

# Read the input and print, waiting one second between readings
while 1:
	if enterZone1.value() :
		zoneNumber = "1"
		print 'EnterZone1'
		#enterZone( zoneNumber )

	if enterZone2.value() :
		zoneNumber = "2"
		print 'EnterZone2'
		#enterZone( zoneNumber )

	if exitZone1.value() :
		zoneNumber = "1"
		print 'ExitZone1'
		#exitZone( zoneNumber )
	
	if exitZone2.value() :
		zoneNumber = "2"
		print 'ExitZone2'
		#exitZone( zoneNumber )
	
	#time.sleep(1)

# Delete the button object
del enterZone1
del enterZone2

# Delete the touch sensor object
del exitZone1
del exitZone2