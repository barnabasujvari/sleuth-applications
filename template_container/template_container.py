import os
import connexion
from flask_cors import CORS
from connexion.resolver import RestyResolver
from waitress import serve

PORT = os.getenv('PORT', 9090)
SERVICE_NAME = 'template_container'

def get_app():
    app = connexion.FlaskApp(__name__, port=PORT, options={'swagger_ui': True}, resolver=RestyResolver('api'))
    app.add_api(
        '../reference/api.yaml',
        arguments={'title': f'Sleuth AI {SERVICE_NAME} Service'},
        strict_validation=True,
        validate_responses=True
    )
    CORS(app.app)
    return app

def main():
    serve(get_app(), host="0.0.0.0", port=PORT)

if __name__ == '__main__':
    serve(get_app(), host="0.0.0.0", port=PORT)
