import jwt
import datetime
import uuid
import gunicorn
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mktoken():
    vizurl = os.environ.get('vizurl')
    tabtoken = jwt.encode(
        {
            "iss": os.environ.get('ClientID'),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": os.environ.get('User'),
            "scp": ["tableau:views:embed", "tableau:metrics:embed"]
        },
        os.environ.get('SecretVal'),
        algorithm="HS256",
        headers={
            'kid': os.environ.get('SecretID'),
            'iss': os.environ.get('ClientID'),
        }
    )
    return render_template('index.html', tabtoken=tabtoken, vizurl=vizurl)


if __name__ == "__main__":
    app.run()
