from sqlalchemy import create_engine
import os
import sys

engine = create_engine("mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb")


result = engine.execute("select * from parks;")

for row in result:
	db_id = row[0]
	park_id = row[1]
	park_name = row[2]
	print("(" + str(db_id) + ", " + park_id + ", " + park_name + ")")