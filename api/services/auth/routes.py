from flask import Blueprint, request, redirect, session, url_for, current_app as app
import requests

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    auth_url = (app.config['AUTH_URL']
                + '?enable_fb_login=0&force_authentication=1&response_type=code'
                + '&client_id=' + app.config['CLIENT_ID']
                + '&redirect_uri=' + app.config['REDIRECT_URI']
                + '&scope=instagram_business_basic,instagram_business_content_publish')
    
    return redirect(auth_url) 

@auth.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "Error: Code not provided by Instagram", 400

    short_token_url = app.config['ACCESS_TOKEN_URL']
    short_payload = {
        'client_id': app.config['CLIENT_ID'],
        'client_secret': app.config['CLIENT_SECRET'],
        'grant_type': 'authorization_code',
        'redirect_uri': app.config['REDIRECT_URI'],
        'code': code
    }

    short_response = requests.post(short_token_url, data=short_payload)
    if short_response.status_code != 200:
        return f"Failed to fetch access token. Response: {response.text}", 400

    short_lived_token = short_response.json().get('access_token')

    long_token_url = app.config['GRAPH_API_URL'] + '/access_token'
    long_payload = {
        'grant_type': 'ig_exchange_token',
        'client_secret': app.config['CLIENT_SECRET'],
        'access_token': short_lived_token
    }

    long_response = requests.get(long_token_url, params=long_payload)
    if long_response.status_code != 200:
        return f"Failed to fetch access token. Response: {long_response.text}", 400

    session['access_token'] = long_response.json().get('access_token')

    return redirect(url_for('home.bio_page'))