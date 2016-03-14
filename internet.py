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

	'''
	html = urllib2.urlopen( url ).read()

	try: js = json.loads(html)
	except: js = None
	'''

	zoneName = "(Enter) Zone " + zoneNumber
	print zoneName

	if zones[int(zoneNumber)] > 0 and zones[int(zoneNumber)] <= limitSpace:
		--zones[int(zoneNumber)]
		availableSpaces()

	else:
		print 'No more space'
		notAvailableSpaces()

	'''
	basePath = "results"

	for i in range( 0, len( js[basePath] ) ):
		firstName = js[basePath][i]["user"]["email"]
		password = js[basePath][i]["user"]["password"]

		print (firstName + '	password: ' + password).encode('utf-8')
	'''

def exitZone( zoneNumber ):
	global zones

	url = "https://randomuser.me/api/?results=" + zoneNumber

	'''
	html = urllib2.urlopen( url ).read()

	try: js = json.loads(html)
	except: js = None
	'''

	zoneName = "(Exit) Zone " + zoneNumber
	print zoneName

	if zones[int(zoneNumber)] >= 0 and zones[int(zoneNumber)] < limitSpace:
		++zones[int(zoneNumber)]
		availableSpaces()
	else:
		print 'Upss;'
		notAvailableSpaces()

	'''
	basePath = "results"

	for i in range( 0, len( js[basePath] ) ):
		firstName = js[basePath][i]["user"]["email"]
		password = js[basePath][i]["user"]["password"]

		print (firstName + '	password: ' + password).encode('utf-8')
	'''