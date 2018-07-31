from sqlalchemy import create_engine
import os
import sys

if os.path.exists("wiki.db"):
	delete_id_number = 4
	engine = create_engine("sqlite:///wiki.db")


	result = engine.execute("select * from wiki where wiki_db_id=:number", number=delete_id_number)
	for row in result:
		#print(row)
		db_id = row[0]
		wiki_title = row[1]
		print("deleteing record: (" + str(db_id) + ", " + wiki_title + ")")


	e = create_engine("sqlite:///wiki.db")

	park_value = 'YELL'
	e.execute("""delete from wiki where wiki_db_id=:number""", 
		number=delete_id_number)
else:
	sys.exit("wiki Table Does Not Exist")