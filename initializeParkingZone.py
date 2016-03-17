import sys
from parkingGeneric import *
import requests

baseAPIUrl = 'https://enigmatic-brushlands-35263.herokuapp.com'

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print 'Error, script must be invoked with the zoneID as an argument'
        print 'Like python createParkingZone.py Z1'
    else:
        zoneID = str(sys.argv[1])
        zonesData = requests.get(baseAPIUrl + '/api/zones').json()
        existingZoneIDs = [z['id'] for z in zonesData]

        if zoneID not in existingZoneIDs:
            print 'Error, the given zoneID doesn\'t correspond to an existing zone.'
        else:
            initParking(zoneID)
            print 'Zone ' + zoneID + ' has been initalized succesfully.'
