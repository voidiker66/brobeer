from sqlalchemy import create_engine
import os
import sys

if os.path.exists("../parksareawesome.db"):
	engine = create_engine("sqlite:///../parksareawesome.db")


	result = engine.execute("select * from parks")
	#result = engine.execute("select * from "
	# "parks where park_name=:name", name='Yellowstone')

	for row in result:
		#print(row)
		db_id = row[0]
		park_id = row[1]
		park_name = row[2]
		park_state = row[3]
		park_description = row[4]
		park_weather = row[5]
		park_lat = row[6]
		park_long = row[7]
		if len(sys.argv) > 1:
			if sys.argv[1] == "-v":
				print("(" + str(db_id) + ", " + park_id + ", " + park_name + ", " + park_state + 
					", " + park_description + ", " + park_weather + ", lat: " + str(park_lat) + ", long:" + str(park_long) +  ")")
		else:
			print("(" + str(db_id) + ", " + park_id + ", " + park_name + ", " + park_state + 
				", lat: " + str(park_lat) + ", long:" + str(park_long) +  ")")
else:
	sys.exit("Parks Table Does Not Exist")