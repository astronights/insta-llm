from flask import Blueprint, session, request, current_app as app
import requests

media = Blueprint('media', __name__)

@media.route('/')
def get_media():

    access_token = request.args.get('access_token')
    page_url = request.args.get('page_url')

    if page_url: 
        posts_response = requests.get(page_url)
    else:
        posts_url = app.config['IG_GRAPH_API_URL']+ '/me/media'
        posts_params = {
            'fields': 'id,caption,media_url,media_type,timestamp,children{id,media_url,media_type},permalink',
            'access_token': access_token
        }
        posts_response = requests.get(posts_url, params=posts_params)

    if posts_response.status_code != 200:
        return f"Failed to fetch posts. Response: {posts_response.text}", 400

    return posts_response.json()

@media.route('/update-caption/<media_id>', methods=['POST'])
def edit_caption(media_id):
    new_caption = request.json.get('caption')
    access_token = session.get('access_token')
    
    url = f"{app.config['IG_GRAPH_API_URL']}/{media_id}"
    payload = {'caption': new_caption}
    params = {'access_token': access_token, 'comment_enabled': True}

    response = requests.post(url, params=params, data=payload)

    return response.json()
