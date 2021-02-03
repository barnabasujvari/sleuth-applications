import os
import json
from pathlib import Path


def search(user, token_info):
    return {"msg": "ok"}, 200


def put(user, token_info, hello_message):
    print(user, token_info, hello_message)
    return {"hello-world-response": f"you sent: {hello_message}"}
