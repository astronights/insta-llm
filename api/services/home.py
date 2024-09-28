from flask import Blueprint, session, request, redirect, url_for, jsonify, current_app as app, render_template
import requests

from datetime import datetime
import time

home = Blueprint('home', __name__)

@home.before_request
def check_authentication():
    access_token = session.get('access_token')
    if not access_token:
        return redirect(url_for('auth.login'))
    
    expires_in, created_time = session.get('expires_in'), session.get('token_created_at')
    if created_time + expires_in - int(time.time()) < 60*60*24:
        requests.get(url_for('auth.refresh', _external=True)).json()
    
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
@home.route('/posts/<string:direction>')
def posts_page(direction=None):
    access_token = session.get('access_token')

    page_url = None
    if direction:
        if direction == 'previous':
            page_url = session.get('page_previous')
        else:
            page_url = session.get('page_next')
    
    media_params = {'access_token': access_token, 'page_url': page_url} 
    media = requests.get(url_for('media.get_media', _external=True), params=media_params).json()

    posts = media['data']
    pages = media['paging']

    for post in posts:
        post['formatted_timestamp'] = datetime.strptime(post['timestamp'][:-5], '%Y-%m-%dT%H:%M:%S').strftime('%d %b, %Y')

    session['page_previous'] = pages.get('previous')
    session['page_next'] = pages.get('next')
    
    return render_template('posts.html', posts=posts, pages=pages)
