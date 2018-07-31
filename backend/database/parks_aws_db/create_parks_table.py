
from sqlalchemy import create_engine


e = create_engine("mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb")

e.execute("""
	create table parks (
		park_db_id INT NOT NULL  AUTO_INCREMENT,
		park_id VARCHAR(5),
		park_name VARCHAR(100),
		park_state VARCHAR(4),
		park_city VARCHAR(100),
		park_description VARCHAR(1000),
		park_weather VARCHAR(1000),
		park_lat VARCHAR(100),
		park_long VARCHAR(100),
		park_phone VARCHAR(20),
		park_phone_display VARCHAR(20),
		park_address VARCHAR(1000),
		park_rating VARCHAR(100),
		park_reviews VARCHAR(100),
		park_image_url VARCHAR(1000),		
		primary key (park_db_id)
	);
""")