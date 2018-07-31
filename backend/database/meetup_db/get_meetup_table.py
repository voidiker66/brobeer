from sqlalchemy import create_engine
import os
import sys

if os.path.exists("../parksareawesome.db"):
	e = create_engine("sqlite:///../parksareawesome.db")


	result = e.execute("select * from meetup")
	#result = engine.execute("select * from "
	# "parks where park_name=:name", name='Yellowstone')

	for row in result:
		db_id = row[0]
		if row[1] != None:
			title = row[1]
		else:
			title = "N/A"


		if row[2] != None:
			summary = row[2]
		else:
			summary = "N/A"

		if row[3] != None:
			image = row[3]
		else:
			image = "N/A"

		if row[4] != None:
			location = row[4]
		else:
			location = "N/A"

		if row[5] != None:
			state = row[5]
		else:
			state = "N/A"

		if row[6] != None:
			country = row[6]
		else:
			country = "N/A"

		if row[7] != None:
			group = row[7]
		else:
			group = "N/A"

		print("(" + str(db_id) + ": " + title + ", " + summary + ", " + str(image) + ")\n")
else:
	sys.exit("meetup Table Does Not Exist")