import time
import pyupm_grove as grove

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