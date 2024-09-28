import os

os.makedirs('api/data', exist_ok=True)

class MetaConfig:
    CLIENT_ID = os.getenv('CLIENT_ID', '')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')
    AUTH_URL = os.getenv('AUTH_URL', '')
    REDIRECT_URI = os.getenv('REDIRECT_URI', '')
    ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'
    GRAPH_API_URL = 'https://graph.instagram.com'

class RedisConfig:
    HOST = 'redis-13928.c9.us-east-1-4.ec2.redns.redis-cloud.com'
    PORT = 13928
    PASS = os.getenv('REDIS_PASS', '')
    
class LLMConfig:    
    API_KEY = os.getenv('API_KEY', '')
