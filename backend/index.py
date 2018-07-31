from flask import Flask,jsonify,request,render_template
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb'
db = SQLAlchemy(app)
CORS(app)
mysql = MySQL()

park_db_col = ["park_db_id", "park_id", "park_name", "park_state", "park_city", "park_description", "park_weather", "park_lat", "park_long", "park_phone", "park_phone_display", "park_address", "park_rating", "park_reviews",  "park_image_url"]
wildlife_db_col = ["wildlife_db_id", "wiki_title", "wiki_summary", "wiki_image"]
meetup_db_col = ["events_db_id", "meetup_title", "meetup_summary", "meetup_image", "meetup_location", "meetup_state", "meetup_country", "meetup_group", "meetup_url", "meetup_time", "meetup_lat", "meetup_long", "meetup_venue_name"]



class Parks(db.Model):
    park_db_id = db.Column(db.Integer, primary_key = True)
    park_id = db.Column(db.String(32), unique = True)
    park_name = db.Column(db.String(100), unique = True)
    park_state = db.Column(db.String(5))
    park_city = db.Column(db.String(32))
    park_description = db.Column(db.String(200), unique = True)
    park_weather = db.Column(db.String(200), unique = True)
    park_lat = db.Column(db.String(100), unique = True)
    park_long = db.Column(db.String(100), unique = True)
    park_address = db.Column(db.String(32), unique = True)
    park_phone = db.Column(db.String(32), unique = True)
    park_phone_display = db.Column(db.String(32), unique = True)
    park_rating = db.Column(db.String(5))
    park_reviews = db.Column(db.String(10))
    park_image_url = db.Column(db.String(40))

class Wildlife(db.Model):
    wildlife_db_id = db.Column(db.Integer, primary_key = True)
    wiki_title = db.Column(db.String(32))
    wiki_summary = db.Column(db.String(200))
    wiki_image = db.Column(db.String(32))

class Events(db.Model):
    events_db_id = db.Column(db.Integer, primary_key = True)
    meetup_title = db.Column(db.String(32))
    meetup_summary = db.Column(db.String(200))
    meetup_image = db.Column(db.String(32))
    meetup_location = db.Column(db.String(32))
    meetup_state = db.Column(db.String(5))
    meetup_country = db.Column(db.String(5))
    meetup_group = db.Column(db.String(32))
    meetup_url = db.Column(db.String(100))
    meetup_time = db.Column(db.String(100))
    meetup_lat = db.Column(db.String(100))
    meetup_long = db.Column(db.String(100))
    meetup_venue_name = db.Column(db.String(100))

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well
manager.create_api(Parks, methods=['GET'],results_per_page=-1)
manager.create_api(Wildlife, methods=['GET'],results_per_page=-1)
manager.create_api(Events, methods=['GET'],results_per_page=-1)

app.config['MYSQL_DATABASE_USER'] = 'vcchau'
app.config['MYSQL_DATABASE_PASSWORD'] = 'parksareawesome'
app.config['MYSQL_DATABASE_DB'] = 'parksareawesomedb'
app.config['MYSQL_DATABASE_HOST'] = 'parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com'
mysql.init_app(app)
conn = mysql.connect()

# Route for first D3 diagram
@app.route('/d3-1')
def usa_map_events():
    return render_template('usa_map_events.html')

# Route for second D3 diagram
@app.route('/d3-2')
def usa_map_d3vis():
    return render_template('usa_map_d3vis.html')

# Route for third D3 diagram
@app.route('/d3-3')
def animals_by_name():
    return render_template('animals_by_name.html')


if __name__ == "__main__":
    app.run(debug = True)
