import os
import json
from pathlib import Path


def search(user, token_info):
    return {"msg": "ok"}, 200


def put(user, token_info, hello_message):
    print(user, token_info, hello_message)
    return {"hello-world-response": f"you sent: {hello_message}"}


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
