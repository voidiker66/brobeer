from sqlalchemy import create_engine
import os


if os.path.exists("../parksareawesome.db"):
	e = create_engine("sqlite:///../parksareawesome.db")
	e.execute("""DROP TABLE IF EXISTS wiki""")