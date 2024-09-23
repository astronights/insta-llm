import os

class MetaConfig:
    CLIENT_ID = os.getenv('CLIENT_ID', '')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')
    REDIRECT_URI = os.getenv('REDIRECT_URI', '')
    AUTHORIZATION_URL = 'https://api.instagram.com/oauth/authorize' #'https://www.facebook.com/v16.0/dialog/oauth'
    ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token' #'https://graph.facebook.com/v16.0/oauth/access_token'
    GRAPH_API_URL = 'https://graph.instagram.com' #'https://graph.instagram.com/me'
    
class LLMConfig:    
    API_KEY = os.getenv('API_KEY', '')
