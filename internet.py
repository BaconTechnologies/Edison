import urllib2
import json

from lcd import *

# Set max capacity 
limitSpace = 10

# Save zone number
zoneNumber = 0

# Save spaces available in zone
spacesAvailable = 0

def init( arg_zoneNumber ):
	global zoneNumber, spacesAvailable, limitSpace

	isAvailable = 0

	# Cast zoneNumber to int
	zoneNumber = int(arg_zoneNumber)

	# Get from REST API spaces available
	spacesAvailable = limitSpace

	# Check if there are available spaces
	if spacesAvailable > 0:
		isAvailable = 1
	else:
		isAvailable = 0

	# Initial display message
	zoneName = "Zone " + str(zoneNumber)
	zoneAvailable = "Available: " + str(spacesAvailable)
	showInScreen( zoneName, zoneAvailable, isAvailable )

def enterZone():
	global limitSpace, zoneNumber, spacesAvailable

	# Declare flag
	isAvailable = 0

	# Set endpoint of REST API
	url = "https://randomuser.me/api/?results=" + str(zoneNumber)

	'''
	html = urllib2.urlopen( url ).read()

	try: js = json.loads(html)
	except: js = None

	basePath = "results"

	for i in range( 0, len( js[basePath] ) ):
		firstName = js[basePath][i]["user"]["email"]
		password = js[basePath][i]["user"]["password"]

		print (firstName + '	password: ' + password).encode('utf-8')
	'''

	# Capacity its in valid range
	if spacesAvailable > 0 and spacesAvailable <= limitSpace:
		spacesAvailable = spacesAvailable - 1

		isAvailable = 1
	else:
		# Parking its full
		print 'No more space'

		isAvailable = 0

	# Check if parking its full
	if spacesAvailable == 0:

		isAvailable = 0

	# Show message at display
	zoneName = "Zone " + str(zoneNumber)
	zoneAvailable = "Available: " + str(spacesAvailable)
	showInScreen( zoneName, zoneAvailable, isAvailable )

def exitZone():
	global limitSpace, zoneNumber, spacesAvailable

	# Declare flag
	isAvailable = 0

	# Set endpoint of REST API
	url = "https://randomuser.me/api/?results=" + str(zoneNumber)

	'''
	html = urllib2.urlopen( url ).read()

	try: js = json.loads(html)
	except: js = None

	basePath = "results"

	for i in range( 0, len( js[basePath] ) ):
		firstName = js[basePath][i]["user"]["email"]
		password = js[basePath][i]["user"]["password"]

		print (firstName + '	password: ' + password).encode('utf-8')
	'''

	# Capacity its in valid range
	if spacesAvailable >= 0 and spacesAvailable < limitSpace:
		#Add one space available
		spacesAvailable = spacesAvailable + 1

		isAvailable = 1
	else:
		#Capacity out of range
		print 'Upss;'

		#Always show positive message
		isAvailable = 1

	# Show message at display
	zoneName = "Zone " + str(zoneNumber)
	zoneAvailable = "Available: " + str(spacesAvailable)
	showInScreen( zoneName, zoneAvailable, isAvailable )