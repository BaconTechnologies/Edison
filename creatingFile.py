import sys

def write():
    print('Creating new text file') 

    extension = ".py"
    zoneID = raw_input('Enter zone ID: ')
    filename = "parkingZone" + str(zoneID) + extension

    declarationImport = 'from parkingGeneric import *\n'
    declarationZoneID = '# Set Zone ID\nzoneID = "' + str(zoneID) + '"\n'
    initializationParking = '# Initialize Parking\ninitParking( zoneID )\n'

    try:
        file = open(filename,'w')   # Trying to create a new file or open one
        
        file.write(declarationImport)
        file.write(declarationZoneID)
        file.write(initializationParking)
        
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

write()