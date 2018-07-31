from sqlalchemy import create_engine
import json
import os
import sys
import re

 
#json_data = open("../json_data/all_parks.json")
#parsed_json = json.loads(json_data)
if os.path.exists("../../parksareawesome.db"):
	e = create_engine("sqlite:///../../parksareawesome.db")
	with open('../../../server/database_json/animals_list_na.json', 'r') as json_data:
		d = json.load(json_data)
		givendata = d["data"]
		for i in givendata:
			wiki_title = i["title"]
			wiki_summary = i["summary"]
			if "image" in i:
				wiki_image = i["image"]
			else:
				wiki_image = None

			e.execute("""insert into wiki(wiki_title, wiki_summary, wiki_image) values 
				(:wikititle, :wikisummary, :wikiimage)""", wikititle=wiki_title,
				wikisummary=wiki_summary, wikiimage=wiki_image)
else:
	sys.exit("wiki Table Does Not Exist")








#if we wanted to insert multiple records into a table, a transaction would need to be created

#conn = engine.connect()
#trans = conn.begin()
#conn.execute("insert into parks (park_id) values ('YELL')")
#conn.execute("insert into parks (park_id) values ('ACAD')")
#trans.commit()
#conn.close()