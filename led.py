import time
import pyupm_grove as grove

# Create the Grove LED object using GPIO pin 2
ledON = grove.GroveLed(2)
ledOFF = grove.GroveLed(6)

enterZone1 = grove.GroveButton(4)
enterZone2 = grove.GroveButton(8)

def availableSpaces():
	global ledON, ledOFF

	ledOFF.off()
	ledON.on()

def notAvailableSpaces():
	global ledON, ledOFF

	ledON.off()
	ledOFF.on()


# Delete the Grove LED object
del ledON
del ledOFF