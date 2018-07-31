from sqlalchemy import create_engine
import os


e = create_engine("sqlite:///../../parksareawesome.db")

if os.path.exists("../../parksareawesome.db"):
	e.execute("""DROP TABLE IF EXISTS parks""")
e.execute("""
	create table parks (
		park_db_id integer primary key,
		park_id varchar,
		park_name varchar,
		park_state varchar,
		park_city varchar,
		park_description varchar,
		park_weather varchar,
		park_lat float,
		park_long float,
		park_phone varchar,
		park_phone_display varchar,
		park_address varchar,
		park_rating float,
		park_reviews integer,
		park_image_url varchar
	)
""")