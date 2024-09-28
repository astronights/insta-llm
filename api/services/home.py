from flask import Blueprint, session, request, redirect, url_for, jsonify, current_app as app, render_template
import requests
import os

home = Blueprint('home', __name__)

@home.before_request
def check_authentication():
    access_token = session.get('access_token')
    if not access_token:
        return redirect(url_for('auth.login'))
    
    if not session.get('profile_data'):
        profile_params = {'access_token': access_token}
        profile = requests.get(url_for('profile.get_profile', _external=True), 
                            params=profile_params).json()
        session['profile_data'] = profile

@home.route('/')
def bio_page():
    profile = session.get('profile_data')    
    return render_template('bio.html', profile=profile)

@home.route('/upload')
def upload_page():
    return render_template('upload.html')

@home.route('/posts')
def posts_page():
    access_token = session.get('access_token')
    
    media_params = {'access_token': access_token, 'url': request.args.get('next_page', None)} 
    media = requests.get(url_for('media.get_media', _external=True), params=media_params).json()

    posts = media['data']
    next_page = media['paging']['next']
    
    return render_template('posts.html', posts=posts, next_page=next_page)
