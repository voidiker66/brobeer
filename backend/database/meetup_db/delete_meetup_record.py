from sqlalchemy import create_engine
import os
import sys

if os.path.exists("meetup.db"):
	delete_id_number = 4
	engine = create_engine("sqlite:///meetup.db")


	result = engine.execute("select * from meetup where meetup_db_id=:number", number=delete_id_number)
	for row in result:
		#print(row)
		db_id = row[0]
		meetup_title = row[1]
		print("deleteing record: (" + str(db_id) + ", " + meetup_title + ")")


	e = create_engine("sqlite:///meetup.db")

	park_value = 'YELL'
	e.execute("""delete from meetup where meetup_db_id=:number""", 
		number=delete_id_number)
else:
	sys.exit("meetup Table Does Not Exist")