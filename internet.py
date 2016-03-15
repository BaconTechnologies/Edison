import urllib2
import json

from led import *

limitSpace = 10
zones = [[], [], []]

for i in range(0, len(zones)):
	zones[i] = limitSpace

def enterZone( zoneNumber ):
	global zones, limitSpace

	url = "https://randomuser.me/api/?results=" + zoneNumber

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

	if zones[zoneNumber] > 0 and zones[zoneNumber] <= limitSpace:
		--zones[zoneNumber]
		availableSpaces()

	else:
		print 'No more space'
		notAvailableSpaces()

	zoneName = "Zone " + str(zoneNumber) + "			Available: " + str(zones[zoneNumber])
	print zoneName

def exitZone( zoneNumber ):
	global zones

	url = "https://randomuser.me/api/?results=" + zoneNumber

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

	if zones[zoneNumber] >= 0 and zones[zoneNumber] < limitSpace:
		++zones[zoneNumber]
		availableSpaces()
	else:
		print 'Upss;'
		notAvailableSpaces()

	zoneName = "Zone " + str(zoneNumber) + "			Available: " + str(zones[zoneNumber])
	print zoneName