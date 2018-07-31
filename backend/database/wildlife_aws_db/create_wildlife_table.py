
from sqlalchemy import create_engine


e = create_engine("mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb")

e.execute("""
	create table wildlife (
		wildlife_db_id INT NOT NULL AUTO_INCREMENT,
		wiki_title VARCHAR(100),
		wiki_summary VARCHAR(1000),
		wiki_image VARCHAR(100),		
		primary key (wildlife_db_id)
	);
""")