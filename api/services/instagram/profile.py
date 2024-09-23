from flask import Blueprint, session, request, redirect, url_for, jsonify, current_app as app, render_template
import requests
import os

profile = Blueprint('profile', __name__)

@profile.route('/')
def get_profile():
    access_token = session.get('access_token')
    if not access_token:
        return redirect(url_for('auth.login'))

    business_profile_url = app.config['GRAPH_API_URL'] + '/me'
    params = {
        'fields': 'id,username,account_type,biography',
        'access_token': access_token
    }

    response = requests.get(business_profile_url, params=params)
    if response.status_code != 200:
        return f"Failed to fetch profile. Response: {response.text}", 400

    profile_data = response.json()
    open(f'api/services/data/{profile_data["id"]}.txt', 'a').close()
    
    media_params = {
        'business_id': profile_data['id'],
        'access_token': access_token
    } 

    user_posts = requests.get(url_for('media.get_media', _external=True), params=media_params)
    posts_data = user_posts.json() 

    return render_template('dashboard.html', profile=profile_data, posts=posts_data)

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
