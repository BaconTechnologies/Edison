import time
import pyupm_grove as grove

# Create the Grove LED object using GPIO pin 2
'''ledON = grove.GroveLed(2)
ledOFF = grove.GroveLed(6)

enterZone1 = grove.GroveButton(4)
enterZone2 = grove.GroveButton(8)'''

def availableSpaces():
	ledON = grove.GroveLed(2)
	ledOFF = grove.GroveLed(6)

	ledOFF.off()
	ledON.on()

def notAvailableSpaces():
	ledON = grove.GroveLed(2)
	ledOFF = grove.GroveLed(6)

	ledON.off()
	ledOFF.on()