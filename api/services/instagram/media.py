from flask import Blueprint, session, request
import requests

media = Blueprint('media', __name__)

@media.route('/')
def get_media():
    access_token = session.get('access_token')
    insta_business_account_id = session.get('instagram_business_account_id')
    
    if insta_business_account_id:
        url = f"{app.config['GRAPH_API_URL']}/{insta_business_account_id}/media"
        response = requests.get(url, params={'access_token': access_token, 'fields': 'id,caption,media_type,media_url,permalink'})
        media_data = response.json()
        return media_data
    
    return "No media found", 404

@media.route('/<media_id>/edit_caption', methods=['POST'])
def edit_caption(media_id):
    new_caption = request.form.get('caption')
    access_token = session.get('access_token')
    
    url = f"{app.config['GRAPH_API_URL']}/{media_id}"
    payload = {'caption': new_caption}
    response = requests.post(url, params={'access_token': access_token}, data=payload)
    return response.json()
