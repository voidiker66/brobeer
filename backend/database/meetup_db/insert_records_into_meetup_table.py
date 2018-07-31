from sqlalchemy import create_engine
import json
import os
import sys
import re

 
#json_data = open("../json_data/all_parks.json")
#parsed_json = json.loads(json_data)
if os.path.exists("../../parksareawesome.db"):
	e = create_engine("sqlite:///../../parksareawesome.db")
	with open('../../../server/database_json/meetup_results.json', 'r') as json_data:
		d = json.load(json_data)
		givendata = d["data"]
		for i in givendata:
			meetup_title = i["name"]
			if "description" in i:
				meetup_summary = i["description"]
			else:
				meetup_summary = None
			if "image" in i:
				meetup_image = i["image"]
			else:
				meetup_image = "https://pbs.twimg.com/profile_images/875701356849504256/x8t7RxeV_400x400.jpg"
			if "venue" in i:
				meetup_location = i["venue"]["address_1"]
				meetup_country = i["venue"]["country"]
				if "state" in i["venue"]:
					meetup_state = i["venue"]["state"]
				else:
					meetup_state = None
			else:
				meetup_location = None
				meetup_country = None
				meetup_state = None	
				
			if "group" in i:
				meetup_group = i["group"]["name"]
			else:
				meetup_group = None		

			e.execute("""insert into meetup(meetup_title, meetup_summary, meetup_image, meetup_location, 
				meetup_state, meetup_country, meetup_group) values (:meetuptitle, :meetupsummary, 
				:meetupimage, :meetuplocation, :meetupstate, :meetupcountry, :meetupgroup)""", 
				meetuptitle=meetup_title, meetupsummary=meetup_summary, meetupimage=meetup_image,
				meetuplocation=meetup_location, meetupstate=meetup_state, meetupcountry=meetup_country,
				meetupgroup=meetup_group)
else:
	sys.exit("meetup Table Does Not Exist")








#if we wanted to insert multiple records into a table, a transaction would need to be created

#conn = engine.connect()
#trans = conn.begin()
#conn.execute("insert into parks (park_id) values ('YELL')")
#conn.execute("insert into parks (park_id) values ('ACAD')")
#trans.commit()
#conn.close()