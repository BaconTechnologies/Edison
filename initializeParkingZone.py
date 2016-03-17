import sys
import urllib2
import json

from parkingGeneric import *

baseAPIUrl = 'https://enigmatic-brushlands-35263.herokuapp.com'
endpoint_zoneDetails = baseAPIUrl + '/api/zones'

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print 'Error, script must be invoked with the zoneID as an argument'
        print 'Like python createParkingZone.py Z1'
    else:
        zoneID = str(sys.argv[1])

        response = urllib2.urlopen( endpoint_zoneDetails ).read()

        try: js = json.loads( response )
        except: js = None

        existingZoneIDs = [js['id'] for z in zonesData]

        if zoneID not in existingZoneIDs:
            print 'Error, the given zoneID doesn\'t correspond to an existing zone.'
        else:
            initParking(zoneID)
            print 'Zone ' + zoneID + ' has been initalized succesfully.'
