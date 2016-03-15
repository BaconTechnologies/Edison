import pyupm_i2clcd as lcd

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS) 
myLcd = lcd.Jhd1313m1(1, 0x3E, 0x62)

# RGB Red
myLcd.setColor(150, 0, 0)

def showInScreen(textUp, textDown, isAvailable):
	global myLcd

	if isAvailable:
		myLcd.setColor(0, 255, 0)
	else:
		myLcd.setColor(255, 0, 0)

	myLcd.clear()

	if len(textUp) > 0:
		myLcd.setCursor(0,0)
		myLcd.write( textUp )

	if len(textDown) > 0:
		myLcd.setCursor(1, 0)
		myLcd.write( textDown )