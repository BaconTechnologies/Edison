import urllib2
import json

def enterZone( zoneNumber ):
	url = "https://randomuser.me/api/?results=" + zoneNumber

	html = urllib2.urlopen( url ).read()

	try: js = json.loads(html)
	except: js = None

	zoneName = "(Enter) Zone " + zoneNumber
	print zoneName

	'''
	basePath = "results"

	for i in range( 0, len( js[basePath] ) ):
		firstName = js[basePath][i]["user"]["email"]
		password = js[basePath][i]["user"]["password"]

		print (firstName + '	password: ' + password).encode('utf-8')
	'''

def exitZone( zoneNumber ):
	url = "https://randomuser.me/api/?results=" + zoneNumber

	html = urllib2.urlopen( url ).read()

	try: js = json.loads(html)
	except: js = None

	zoneName = "(Exit) Zone " + zoneNumber
	print zoneName

	'''
	basePath = "results"

	for i in range( 0, len( js[basePath] ) ):
		firstName = js[basePath][i]["user"]["email"]
		password = js[basePath][i]["user"]["password"]

		print (firstName + '	password: ' + password).encode('utf-8')
	'''