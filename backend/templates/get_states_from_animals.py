from sqlalchemy import create_engine
import os
import sys

engine = create_engine("mysql+pymysql://vcchau:parksareawesome@parksareawesome.chr9q1gt6nxw.us-east-1.rds.amazonaws.com:3306/parksareawesomedb")



states = ["HI", "AK", "FL", "NH", "MI", "VT", "ME", "RI", "NY", "PA", "NJ", "DE",
		"MD", "VA", "WV", "OH", "IN", "IL", "CT", "WI", "NC", "MA", "TN", "AR", "MO",
		"GA", "SC", "KY", "AL", "LS", "MS", "IA", "MN", "OK", "TX", "NM", "KS", "NE",
		"SD", "ND", "WY", "MT", "CO", "ID", "UT", "AZ", "NV", "OR", "WA", "CA"]

for item in states:
	state_dict[item] = 0

result = engine.execute("select wildlife_state from wildlife;")

for state in result:
	state_dict[state[0].upper()] = state_dict[state[0].upper()] + 1


for key in state_dict:
	f = open('state_wildlife', 'w')
	f.truncate(0);
	f.write(key + ',' + state_dict[key])
	f.close()


