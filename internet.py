import urllib2
import json

from lcd import *

# Set max capacity 
limitSpace = 10

# Save zone ID
zoneID = 0

# Save spaces available in zone
spacesAvailable = 0

# Host details
host = "http://10.43.54.5:8000"
endpoint_zoneDetails = host + "/api/zone"
endpoint_zoneEnter = host + "/api/zone" # /api/zone/:zoneID/enter
endpoint_zoneExit = host + "/api/zone"  # /api/zone/:zoneID/exit

def init( arg_zoneID ):
	global host, endpoint_zoneDetails, endpoint_zoneEnter, endpoint_zoneExit, zoneID, spacesAvailable, limitSpace

	isAvailable = 0

	# Set zoneID
	zoneID = str(arg_zoneID)

	# Configure endpoints
	endpoint_zoneDetails = endpoint_zoneDetails + "/" + zoneID
	endpoint_zoneEnter = endpoint_zoneEnter + "/" + zoneID + "/enter"
	endpoint_zoneExit = endpoint_zoneExit + "/" + zoneID + "/exit"

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
	global endpoint_zoneEnter, limitSpace, zoneID, spacesAvailable, zoneName

	# Declare flag
	isAvailable = 0

	# Fields of endpoint result
	capacity_field = "capacity"
	occupancy_field = "occupancy"
	availability_field = "availability"
	zoneName_field = "name"
	zoneID_field = "id"

	response = urllib2.urlopen( endpoint_zoneEnter ).read()

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
	global endpoint_zoneExit, limitSpace, zoneID, spacesAvailable, zoneName

	# Declare flag
	isAvailable = 0

	# Fields of endpoint result
	capacity_field = "capacity"
	occupancy_field = "occupancy"
	availability_field = "availability"
	zoneName_field = "name"
	zoneID_field = "id"

	response = urllib2.urlopen( endpoint_zoneExit ).read()

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