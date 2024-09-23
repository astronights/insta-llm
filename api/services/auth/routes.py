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

    token_url = app.config['ACCESS_TOKEN_URL']
    payload = {
        'client_id': app.config['CLIENT_ID'],
        'client_secret': app.config['CLIENT_SECRET'],
        'grant_type': 'authorization_code',
        'redirect_uri': app.config['REDIRECT_URI'],
        'code': code
    }

    response = requests.post(token_url, data=payload)
    if response.status_code != 200:
        return f"Failed to fetch access token. Response: {response.text}", 400

    access_token_data = response.json()

    session['access_token'] = access_token_data.get('access_token')

    return redirect(url_for('profile.get_profile'))