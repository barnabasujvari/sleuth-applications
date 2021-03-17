import os
import six
from werkzeug.exceptions import Unauthorized
import requests
from google.oauth2 import id_token
from google.auth.transport import requests
import json

CLIENT_ID = os.getenv('CLIENT_ID')

def decode_token(token):
    try:
        if os.getenv("DISABLE_OAUTH") != "True":
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            userid = idinfo["sub"]
            return idinfo
        else:
            return json.load(open("tests/test_jwt.json"))
    except ValueError as e:
        # Invalid token
        six.raise_from(Unauthorized, e)