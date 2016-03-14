import urllib2
import json

from led import *

zones = [[], []]

def enterZone( zoneNumber ):
	global zones

	url = "https://randomuser.me/api/?results=" + zoneNumber

	'''
	html = urllib2.urlopen( url ).read()

	try: js = json.loads(html)
	except: js = None
	'''

	zoneName = "(Enter) Zone " + zoneNumber
	print zoneName

	if zones[zoneNumber] < 10:
		++zones[zoneNumber]
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

	if zones[zoneNumber] > 0 && zones[zoneNumber] <= 10:
		--zones[zoneNumber]
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