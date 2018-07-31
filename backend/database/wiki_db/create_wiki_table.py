from sqlalchemy import create_engine
import os


e = create_engine("sqlite:///../../parksareawesome.db")

if os.path.exists("../../parksareawesome.db"):
	e.execute("""DROP TABLE IF EXISTS wiki""")
e.execute("""
	create table wiki (
		wiki_db_id integer primary key,
		wiki_title varchar,
		wiki_summary varchar,
		wiki_image varchar
	)
""")