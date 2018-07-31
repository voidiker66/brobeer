
from sqlalchemy import create_engine
import json
import os
import sys
import re

 
#json_data = open("../json_data/all_parks.json")
#parsed_json = json.loads(json_data)
e = create_engine("mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb")
with open('../../database_json/combined_park_data.json', 'r') as json_data:
	d = json.load(json_data)
	givendata = d["data"]
	for i in givendata:
		park_value = i["parkCode"]
		given_name = i["fullName"]
		park_state = i["states"]
		park_description = i["description"]
		park_weather = i["weatherInfo"]

		park_lat_long = i["latLong"] if i["latLong"] else "lat:None, long:None"
		park_lat, park_long = park_lat_long.split(", ")
		park_lat = re.findall("\d+\.\d+", park_lat)
		park_long = re.findall("\d+\.\d+", park_long)		
		parklat = float(park_lat[0]) if park_lat else None
		parklong  = float(park_long[0]) if park_long else None

		if "location" in i:
			park_city = i["location"]["city"]
			park_address = i["location"]["address1"]
		else:
			park_city = None
			park_address = None
		if "rating" in i:
			park_rating = i["rating"]
		else:
			park_rating = None
		if "review_count" in i:
			park_reviews = i["review_count"]
		else:
			park_reviews = None
		if "phone" in i:
			park_phone = i["phone"]
		else:
			park_phone = None
		if "display_phone" in i:
			park_phone_display = i["display_phone"]
		else:
			park_phone_display = None
		if "image_url" in i:
			if len(i["image_url"]) < 1:
				park_image_url = "http://www.documenta14.de/images/d14_Karlsaue_%C2%A9_Mathias_Voelzke-web-001.jpg,1440"
			else:
				park_image_url = i["image_url"]
		else:
			park_image_url = "http://www.documenta14.de/images/d14_Karlsaue_%C2%A9_Mathias_Voelzke-web-001.jpg,1440"


		#execute_instr = "INSERT INTO parks(park_id, park_name) VALUES (park_value, given_name);"
		print(park_value + " :  " + given_name)
		e.execute("""INSERT INTO parks(park_id, park_name, park_state, park_city, park_description, park_weather, 
				park_lat, park_long, park_phone, park_phone_display, park_address, park_rating, park_reviews, park_image_url) 
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
				park_value, given_name, park_state, park_city, park_description, park_weather, 
				parklat, parklong, park_phone, park_phone_display, park_address, park_rating, park_reviews, park_image_url)








#if we wanted to insert multiple records into a table, a transaction would need to be created

#conn = engine.codnnect()
#trans = conn.begin()
#conn.execute("insert into parks (park_id) values ('YELL')")
#conn.execute("insert into parks (park_id) values ('ACAD')")
#trans.commit()
#conn.close()