from flask import Blueprint, session, request, jsonify
import requests

profile = Blueprint('profile', __name__)

# Fetch Instagram Business Profile Info including bio
@profile.route('/')
def get_profile():
    access_token = session.get('access_token')
    insta_business_account_id = session.get('instagram_business_account_id')
    
    if insta_business_account_id:
        url = f"{app.config['GRAPH_API_URL']}/{insta_business_account_id}"
        params = {
            'fields': 'username,media_count,biography',
            'access_token': access_token
        }
        response = requests.get(url, params=params)
        profile_data = response.json()
        return profile_data
    
    return jsonify({"error": "Profile not found"}), 404


# Update Instagram Business Profile Bio
@profile.route('/update_bio', methods=['POST'])
def update_bio():
    new_bio = request.form.get('bio')
    access_token = session.get('access_token')
    page_id = session.get('facebook_page_id')  # Instagram Business Profile is linked to a Facebook Page

    if page_id and new_bio:
        # You can update bio via Facebook Page API
        url = f"https://graph.facebook.com/{page_id}"
        payload = {
            'about': new_bio,
            'access_token': access_token
        }
        response = requests.post(url, data=payload)
        return response.json()
    
    return jsonify({"error": "Unable to update bio"}), 400
