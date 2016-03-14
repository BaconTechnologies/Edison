import time
import pyupm_grove as grove

# Create the Grove LED object using GPIO pin 2
ledON = grove.GroveLed(2)
ledOFF = grove.GroveLed(6)

def availableSpaces():
	ledOFF.off()
	ledON.on()

def notAvailableSpaces():
	ledON.off()
	ledOFF.on()

# Delete the Grove LED object
del ledON
del ledOFF