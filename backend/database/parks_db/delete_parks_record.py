from sqlalchemy import create_engine
import os
import sys

if os.path.exists("parks.db"):
	delete_id_number = 4
	engine = create_engine("sqlite:///parks.db")


	result = engine.execute("select * from parks where park_db_id=:number", number=delete_id_number)
	for row in result:
		#print(row)
		db_id = row[0]
		park_id = row[1]
		park_name = row[2]
		print("deleteing record: (" + str(db_id) + ", " + park_id + ", " + park_name + ")")


	e = create_engine("sqlite:///parks.db")

	park_value = 'YELL'
	e.execute("""delete from parks where park_db_id=:number""", 
		number=delete_id_number)
else:
	sys.exit("Parks Table Does Not Exist")