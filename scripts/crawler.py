import requests
import json
import time

next_page = 'https://graph.instagram.com/me/media'

token = ''
params = {
    'fields': 'id,caption,media_url,media_type,timestamp,children{id,media_url,media_type},permalink',
    'access_token': token
}

c = 0
all_posts = []

while next_page:
    
    start = time.time()
    res = requests.get(next_page, params=params).json()

    posts = res['data']
    pages = res['paging']

    all_posts.extend(posts)
    print(f'Time: {(time.time() - start):.2f}s: {len(posts)} [All: {len(all_posts)}]')

    next_page = pages.get('next', None)

with open('./posts.json', 'w') as f:
    json.dump(all_posts, f)