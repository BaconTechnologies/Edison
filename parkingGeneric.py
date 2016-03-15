import time
import pyupm_grove as grove
import pyupm_ttp223 as ttp223

from internet import *

def initParking( zoneID ):
	# Create button sensor in D4
	pinEnter = 4
	enterZone1 = grove.GroveButton( pinEnter )

	# Create touch sensor in D3
	pinExit = 3
	exitZone1 = ttp223.TTP223( pinExit )

	# Initial configuration
	init( zoneID )

	# Read the input and print, waiting one second between readings
	while 1:
		# Enter Zone detection
		if enterZone1.value() :
			print 'Enter'
			enterZone()

		# Exit Zone detection
		if exitZone1.value() :
			print 'Exit'
			exitZone()
		
		# Wait 1 second
		time.sleep(1)

	# Delete the button object
	del enterZone1

	# Delete the touch sensor object
	del exitZone1