import sys

def write():
    print('Creating new text file') 

    extension = ".py"
    filename = "parkingZone" + raw_input('Enter zone ID: ') + extension

    declarationImport = 'from parkingGeneric import *'
    declarationZoneID = '# Set Zone ID\nzoneID = "zona1"'
    initializationParking = '# Initialize Parking\ninitParking( zoneID )'

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