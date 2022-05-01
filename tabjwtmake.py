import jwt
import datetime
import uuid
import os

def mktoken():
    token = jwt.encode(
	{
		"iss": os.getenv('ClientID'), #ClientID
		"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
		"jti": str(uuid.uuid4()),
		"aud": "tableau",
		"sub": os.getenv('UserID'), #User
		"scp": ["tableau:views:embed", "tableau:metrics:embed"]
	},
		os.getenv('SecretVal'), #SecretVal
		algorithm = "HS256",
		headers = {
		'kid': os.getenv('SecretID'), #SecretID
		'iss': os.getenv('ClientID') #ClientID
        }
  )
    return token