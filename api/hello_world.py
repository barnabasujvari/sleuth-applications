def search():
    return {'msg': 'ok'}, 200

def put(body):
    return {
        "hello-world-response": f"you sent: {body['hello_message']}"
    }