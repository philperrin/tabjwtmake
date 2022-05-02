import jwt
import datetime
import uuid
# import os

def mktoken():
    token = jwt.encode(
	{
		"iss": '159802a9-bc87-46df-9635-93b75a01a631', #ClientID
		"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
		"jti": str(uuid.uuid4()),
		"aud": "tableau",
		"sub": 'pperrin@phdata.io', #User
		"scp": ["tableau:views:embed", "tableau:metrics:embed"]
	},
		'VdzA3pZ8Dek91znHR7HQWocCSo6FUQ9rF8fhpK2L+ig=', #SecretVal
		algorithm = "HS256",
		headers = {
		'kid': '47cd7668-0308-4652-91d6-e42c13b5bbb4', #SecretID
		'iss': '159802a9-bc87-46df-9635-93b75a01a631' #ClientID
        }
  )
    return token