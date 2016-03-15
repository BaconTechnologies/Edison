import urllib2
import json

from lcd import *

# Set max capacity 
limitSpace = 10

# Save zone ID
zoneID = 0

# Save spaces available in zone
spacesAvailable = 0

def init( arg_zoneID ):
	global zoneID, spacesAvailable, limitSpace

	isAvailable = 0

	zoneID = str(arg_zoneID)

	endpoint = "http://10.43.54.5:8000/api/zone/" + zoneID

	# Fields of endpoint result
	capacity_field = "capacity"
	occupancy_field = "occupancy"
	availability_field = "availability"
	zoneName_field = "name"
	zoneID_field = "id"

	response = urllib2.urlopen( endpoint ).read()

	try: js = json.loads( response )
	except: js = None

	# Get from REST API zone name
	zoneName = str(js[zoneName_field])

	# Get from REST API limit spaces
	limitSpace = int(js[capacity_field])

	# Get from REST API spaces available
	spacesAvailable = int(js[availability_field])

	# Check if there are available spaces
	if spacesAvailable > 0:
		isAvailable = 1
	else:
		isAvailable = 0

	# Initial display message
	zoneAvailable = "Available: " + str(spacesAvailable)
	showInScreen( zoneName, zoneAvailable, isAvailable )

def enterZone():
	global limitSpace, zoneID, spacesAvailable, zoneName

	# Declare flag
	isAvailable = 0

	# Set endpoint of REST API of enter zone
	endpoint = "http://10.43.54.5:8000/api/zone/" + zoneID + "/enter"

	# Fields of endpoint result
	capacity_field = "capacity"
	occupancy_field = "occupancy"
	availability_field = "availability"
	zoneName_field = "name"
	zoneID_field = "id"

	response = urllib2.urlopen( endpoint ).read()

	try: js = json.loads( response )
	except: js = None

	zoneName = str(js[zoneName_field])
	spacesAvailable = int(js[availability_field])

	# Check if parking its full
	if spacesAvailable <= 0:
		isAvailable = 0
	else:
		isAvailable = 1

	# Show message at display
	zoneAvailable = "Available: " + str(spacesAvailable)
	showInScreen( zoneName, zoneAvailable, isAvailable )

def exitZone():
	global limitSpace, zoneID, spacesAvailable, zoneName

	# Declare flag
	isAvailable = 0

	# Set endpoint of REST API of exit zone
	endpoint = "http://10.43.54.5:8000/api/zone/" + zoneID + "/exit"

	# Fields of endpoint result
	capacity_field = "capacity"
	occupancy_field = "occupancy"
	availability_field = "availability"
	zoneName_field = "name"
	zoneID_field = "id"

	response = urllib2.urlopen( endpoint ).read()

	try: js = json.loads( response )
	except: js = None

	zoneName = str(js[zoneName_field])
	spacesAvailable = int(js[availability_field])

	# There is enough space
	if spacesAvailable > 0:
		isAvailable = 1

	# Show message at display
	zoneAvailable = "Available: " + str(spacesAvailable)
	showInScreen( zoneName, zoneAvailable, isAvailable )