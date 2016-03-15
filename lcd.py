import pyupm_i2clcd as lcd

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS) 
display = lcd.Jhd1313m1(1, 0x3E, 0x62)

# Set Background Color of Display
display.setColor(150, 0, 0)

def showInScreen(textUp, textDown, isAvailable):
	global display

	# Check if its available; change to green, otherwise change to red
	if isAvailable:
		display.setColor(0, 255, 0)
	else:
		display.setColor(255, 0, 0)

	# Clear display
	display.clear()

	# Check if text up was fullfilled
	if len(textUp) > 0:
		display.setCursor(0,0)

		# Set Text on Display
		display.write( textUp )

	# Check if text down was fullfilled
	if len(textDown) > 0:
		display.setCursor(1, 0)

		# Set Text on Display
		display.write( textDown )