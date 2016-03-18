Parking brain Stable version

Installation
Its very easy to implement one or more modules (Porkys), you just need to clone the git repository on the Edison board:
	git clone https://github.com/BaconTechnologies/Edison.git

if you dont have git installed, follow this commands:
	https://github.com/w4ilun/edison-guides/wiki/Installing-Git-on-Intel-Edison

After you had cloned the repository
Create a parking zone through our easy dashboard:
	https://desolate-sands-40235.herokuapp.com/dashboard

Selecting the "Details" tab and in the section "Parking Lots Details" there are two ways to create them, you can import an csv with the format (yellow empty file):
	# Id zone, # id slot, Available/Occupancy (1 or 0)

	ex:
		A, 1, 0
		A, 2, 1
		B, 1, 1
		...

Or creating one by one through the "Create parking zone" button (blue plus sign) and adding the id zone, name of the zone, capacity and occupancy.

Your porky its almost done, just need to execute on Edison board the file "initializeParkingZone.py" using this format:
	python initializeParkingZone.py ID_ZONE

	ex:
		python initializeParkingZone.py A

Perfect!, your porky its ON!
