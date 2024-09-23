import os

os.makedirs('api/services/data', exist_ok=True)

class MetaConfig:
    CLIENT_ID = os.getenv('CLIENT_ID', '')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')
    AUTH_URL = os.getenv('AUTH_URL', '')
    REDIRECT_URI = os.getenv('REDIRECT_URI', '')
    ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'
    GRAPH_API_URL = 'https://graph.instagram.com'
    
class LLMConfig:    
    API_KEY = os.getenv('API_KEY', '')
