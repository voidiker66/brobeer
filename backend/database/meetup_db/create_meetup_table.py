from sqlalchemy import create_engine
import os

e = create_engine("sqlite:///../../parksareawesome.db")

if os.path.exists("../../parksareawesome.db"):
	e.execute("""DROP TABLE IF EXISTS meetup""")
e.execute("""
	create table meetup (
		meetup_db_id integer primary key,
		meetup_title varchar,
		meetup_summary varchar,
		meetup_image varchar,
		meetup_location varchar,
		meetup_state varchar,
		meetup_country varchar,
		meetup_group varchar
	)
""")