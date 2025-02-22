from .services.instagram.profile import profile
from .services.instagram.media import media
from .services.instagram.post import post
from .services.auth.routes import auth
from .services.home import home
from .services.genai.llm import llm
from .config import MetaConfig, LLMConfig, RedisConfig

import json
import logging

from uuid import uuid4
from redis import Redis

from flask import Flask, send_from_directory, request, jsonify
from flask_session import Session

def create_app():
    app = Flask(__name__)
    app.secret_key = str(uuid4())
    
    # Load configuration (API keys, secrets)
    app.config.from_object(MetaConfig)
    app.config.from_object(LLMConfig)

    # Register blueprints
    app.register_blueprint(home, url_prefix='/home')
    app.register_blueprint(profile, url_prefix='/profile')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(media, url_prefix='/media')
    app.register_blueprint(post, url_prefix='/post')
    app.register_blueprint(llm, url_prefix='/llm')

    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = Redis(host=RedisConfig.HOST, port=RedisConfig.PORT, 
                                        password=RedisConfig.PASS)

    Session(app)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    from flask import send_from_directory

    @app.route('/favicon')
    def favicon():
        return send_from_directory('static', 'favicon.ico')

    return app

app = create_app()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.before_request
def log_request_info():
    logging.info(f'Received request: {request.method} {request.url}')
    logging.info(f'Headers: {dict(request.headers)}')
    if request.is_json:
        logging.info(f'Payload: {request.get_json()}')

@app.after_request
def log_response_info(response):
    logging.info(f'Response status: {response.status}')

    if response.is_json:
        try:
            response_data = json.loads(response.get_data(as_text=True))
            logging.info(f"Response data: {json.dumps(response_data, indent=2)}")
        except Exception as e:
            logging.error(f"Failed to log response body: {e}")
    return response

# Entry point for Vercel
def main(request):
    # Use request context for Flask
    with app.request_context(request):
        return app.full_dispatch_request()

# For local development
if __name__ == '__main__':
    app.run(debug=True)
