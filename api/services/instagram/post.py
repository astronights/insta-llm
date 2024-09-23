from flask import Blueprint, session, request, current_app as app
import requests

post = Blueprint('post', __name__)

@post.route('/create', methods=['POST'])
def create_post():
    access_token = session.get('access_token')
    insta_business_account_id = session.get('instagram_business_account_id')
    
    image_url = request.form.get('image_url')
    caption = request.form.get('caption')
    
    if insta_business_account_id:
        # Step 1: Create a media object
        create_media_url = f"{app.config['GRAPH_API_URL']}/{insta_business_account_id}/media"
        media_payload = {
            'image_url': image_url,
            'caption': caption,
            'access_token': access_token
        }
        media_response = requests.post(create_media_url, data=media_payload)
        media_data = media_response.json()
        
        # Step 2: Publish the media object
        creation_id = media_data.get('id')
        publish_url = f"{app.config['GRAPH_API_URL']}/{insta_business_account_id}/media_publish"
        publish_payload = {
            'creation_id': creation_id,
            'access_token': access_token
        }
        publish_response = requests.post(publish_url, data=publish_payload)
        return publish_response.json()
    
    return "Unable to post", 400
