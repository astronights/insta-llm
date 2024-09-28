import requests
import json
import time

GRAPH_API = 'https://graph.instagram.com'
MONGO_URI = 'mongodb://localhost:27017/' 

DB_NAME = 'instagram_data'
COLLECTION_NAME = 'user_posts'


def get_all_media_posts(access_token):
    media_posts = []
    next_page = f'{GRAPH_API}/me/media'
    
    while next_page:
        params = {
            'fields': 'id,caption,media_url,media_type,timestamp,children{id,media_url,media_type},permalink',
            'access_token': access_token
        }
        
        response = requests.get(next_page, params=params)
        data = response.json()

        # Process the current page and upsert each post
        for post in data.get('data', []):
            upsert_to_mongodb(post)

        # Continue to the next page, if it exists
        next_page = data.get('paging', {}).get('next', None)
    
    return media_posts

# Use requests to upsert to MongoDB Data API
def upsert_to_mongodb(post):
    mongo_url = f"{MongoDB.ATLAS_DATA_API_URL}/action/updateOne"
    
    headers = {
        'Content-Type': 'application/json',
        'api-key': MongoDB.API_KEY
    }

    # MongoDB filter: match post by ID
    filter_doc = {'id': post['id']}

    # The update document: upsert the post data
    update_doc = {
        '$set': post
    }

    # Specify that the operation should upsert
    payload = {
        'collection': MongoDB.COLLECTION_NAME,
        'database': MongoDB.DB_NAME,
        'dataSource': MongoDB.DATA_SOURCE,
        'filter': filter_doc,
        'update': update_doc,
        'upsert': True
    }

    # Perform the update (upsert) operation
    response = requests.post(mongo_url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        print(f"Failed to upsert record: {response.text}")
    else:
        print(f"Upserted post with ID: {post['id']}")

def refresh_posts(token, profile_id):
        save_all_media_posts(token)

if __name__ == '__main__':
    refresh_posts(token, profile_id)