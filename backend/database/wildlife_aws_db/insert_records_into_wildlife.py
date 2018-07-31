from sqlalchemy import create_engine
import json
import sys
import re

 
#json_data = open("../json_data/all_parks.json")
#parsed_json = json.loads(json_data)
e = create_engine("mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb")
with open('../../database_json/animals_list_na.json', 'r') as json_data:
	d = json.load(json_data)
	givendata = d["data"]
	for i in givendata:
		wiki_title = i["title"]
		wiki_summary = i["summary"]
		if "image" in i:
			wiki_image = i["image"]
		else:
			wiki_image = None
		print(wiki_title)
		e.execute("""insert into wildlife(wiki_title, wiki_summary, wiki_image) values 
			(%s, %s, %s);""", wiki_title, wiki_summary, wiki_image)