from flask import Blueprint, session, request, current_app as app
import requests

media = Blueprint('media', __name__)

@media.route('/')
def get_media():
    igid = request.args.get('business_id')
    access_token = request.args.get('access_token')
    
    # posts_url = app.config['GRAPH_API_URL'] + f'/v20.0/{igid}/media'
    posts_url = app.config['GRAPH_API_URL']+ '/me/media'
    posts_params = {
        'fields': 'id,caption,media_url,media_type',
        'access_token': access_token
    }

    print(posts_url, posts_params)

    posts_response = requests.get(posts_url, params=posts_params)
    print(posts_response)
    if posts_response.status_code != 200:
        return f"Failed to fetch posts. Response: {posts_response.text}", 400
    
    

    posts_data = posts_response.json().get('data', [])

    return posts_data

@media.route('/<media_id>/edit_caption', methods=['POST'])
def edit_caption(media_id):
    new_caption = request.form.get('caption')
    access_token = session.get('access_token')
    
    url = f"{app.config['GRAPH_API_URL']}/{media_id}"
    payload = {'caption': new_caption}
    response = requests.post(url, params={'access_token': access_token}, data=payload)
    return response.json()
