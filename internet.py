import urllib2
import json

from led import *
from lcd import *

# Set max capacity 
limitSpace = 10
zones = [[], [], []]

# Init max capacity of each zone
for i in range(0, len(zones)):
	zones[i] = limitSpace

def enterZone( zoneNumber ):
	global zones, limitSpace

	url = "https://randomuser.me/api/?results=" + zoneNumber

	# Cast zoneNumber to int (get from REST API)
	zoneNumber = int(zoneNumber)

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
	if zones[zoneNumber] > 0 and zones[zoneNumber] <= limitSpace:
		zones[zoneNumber] = zones[zoneNumber] - 1
		availableSpaces()
	else:
		# Parking its full
		print 'No more space'
		notAvailableSpaces()

	# Check if parking its full
	if zones[zoneNumber] == 0:
		notAvailableSpaces()

	zoneName = "Zone " + str(zoneNumber) + "			Available: " + str(zones[zoneNumber])
	showInScreen( zoneName )

def exitZone( zoneNumber ):
	global zones

	url = "https://randomuser.me/api/?results=" + zoneNumber

	# Cast zoneNumber to int (get from REST API)
	zoneNumber = int(zoneNumber)

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
	if zones[zoneNumber] >= 0 and zones[zoneNumber] < limitSpace:
		zones[zoneNumber] = zones[zoneNumber] + 1
		availableSpaces()
	else:
		#Capacity out of range
		print 'Upss;'
		notAvailableSpaces()

	zoneName = "Zone " + str(zoneNumber) + "			Available: " + str(zones[zoneNumber])
	showInScreen( zoneName )