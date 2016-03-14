import urllib2
import json

def request( whereAreYouGoing ):
	url = "https://randomuser.me/api/?results=", whereAreYouGoing
	html = urllib2.urlopen( url ).read()

	try: js = json.loads(html)
	except: js = None

	basePath = "results"

	for i in range( 0, len( js[basePath] ) ):
		firstName = js[basePath][i]["user"]["name"]["first"]
		gender = js[basePath][i]["user"]["gender"]

		print firstName, '	gender: ', gender