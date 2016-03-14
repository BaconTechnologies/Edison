import pyupm_i2clcd as lcd
import time

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS) 
myLcd = lcd.Jhd1313m1(1, 0x3E, 0x62)
myLcd.setCursor(0,0)
# RGB Blue
#myLcd.setColor(53, 39, 249)

# RGB Red
myLcd.setColor(250, 0, 0)

myLcd.write('Hello World')
myLcd.setCursor(1,2)
myLcd.write('Hello World2')

while 1:
	time.sleep(1)