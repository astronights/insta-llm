from flask import Blueprint, session, request, redirect, url_for, jsonify, current_app as app, render_template
import requests
import os

home = Blueprint('home', __name__)

@home.before_request
def check_authentication():
    # This will run before any request to the `home` routes
    access_token = session.get('access_token')
    if not access_token:
        # Redirect to the login page if not authenticated
        return redirect(url_for('auth.login'))
    
    if not session['profile_data']:
        profile_params = {'access_token': access_token}
        profile = requests.get(url_for('profile.get_profile', _external=True), 
                            params=profile_params).json()
        session['profile_data'] = profile

@home.route('/')
def bio_page():
    access_token = session.get('access_token')
    
    profile = session.get('profile_data')
    
    # media_params = {'business_id': profile['id'], 'access_token': access_token} 
    # media = requests.get(url_for('media.get_media', _external=True), 
    #                      params=media_params).json()
    
    return render_template('bio.html', profile=profile)

@home.route('/upload')
def upload_page():
    return render_template('upload.html')

@home.route('/posts')
def posts_page():
    access_token = session.get('access_token')
    profile = session.get('profile_data')
    
    media_params = {'business_id': profile['id'], 'access_token': access_token} 
    media = requests.get(url_for('media.get_media', _external=True), 
                         params=media_params).json()
    
    return render_template('posts.html', posts=media)
