import os

os.makedirs('api/data', exist_ok=True)

class MetaConfig:
    IG_CLIENT_ID = os.getenv('CLIENT_ID', '')
    IG_CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')
    IG_AUTH_URL = os.getenv('AUTH_URL', '')
    IG_REDIRECT_URI = os.getenv('REDIRECT_URI', '')
    IG_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'
    IG_GRAPH_API_URL = 'https://graph.instagram.com'

class RedisConfig:
    HOST = 'redis-19906.c292.ap-southeast-1-1.ec2.redns.redis-cloud.com'
    PORT = 19906
    PASS = os.getenv('REDIS_PASS', '')
    
class LLMConfig:    
    LLM_API_KEY = os.getenv('API_KEY', '')
