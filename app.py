import jwt
import datetime
import uuid
import gunicorn
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def mktoken():
	tabtoken = jwt.encode(
	{
		"iss": os.environ.get('ClientID'), #'159802a9-bc87-46df-9635-93b75a01a631', #ClientID
		"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
		"jti": str(uuid.uuid4()),
		"aud": "tableau",
		"sub": os.environ.get('User'), #'pperrin@phdata.io', #User
		"scp": ["tableau:views:embed", "tableau:metrics:embed"]
	},
		os.environ.get('SecretVal'), #'VdzA3pZ8Dek91znHR7HQWocCSo6FUQ9rF8fhpK2L+ig=', #SecretVal
		algorithm = "HS256",
		headers = {
		'kid': os.environ.get('SecretID'), #'47cd7668-0308-4652-91d6-e42c13b5bbb4', #SecretID
		'iss': os.environ.get('ClientID'), #'159802a9-bc87-46df-9635-93b75a01a631' #ClientID
		}
	)
	return tabtoken

if __name__ == "__main__":
    app.run()