from sqlalchemy import create_engine
import os
import sys

if os.path.exists("../parksareawesome.db"):
	engine = create_engine("sqlite:///../parksareawesome.db")


	result = engine.execute("select * from wiki")
	#result = engine.execute("select * from "
	# "parks where park_name=:name", name='Yellowstone')

	for row in result:
		#print(row)
		db_id = row[0]
		title = row[1]
		summary = row[2]
		image = row[3]

		print(str(db_id) + ": " + title + ", " + summary + ", " + str(image) + "\n")
else:
	sys.exit("wiki Table Does Not Exist")