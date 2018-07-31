from sqlalchemy import create_engine
import os
import sys

engine = create_engine("mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb")


result = engine.execute("select * from wildlife;")

for row in result:
	db_id = row[0]
	wiki_title = row[1]
	wiki_summary = row[2]
	print("(" + str(db_id) + ", " + wiki_title + ", " + wiki_summary + ")")