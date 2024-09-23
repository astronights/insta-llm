from flask import Blueprint, request, redirect, session, url_for
import requests

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    auth_url = f"{app.config['AUTHORIZATION_URL']}?client_id={app.config['CLIENT_ID']}&redirect_uri={app.config['REDIRECT_URI']}&scope=pages_show_list,instagram_basic,instagram_manage_insights,instagram_manage_comments&response_type=code"
    return redirect(auth_url)

@auth.route('/callback')
def callback():
    code = request.args.get('code')
    token_url = app.config['ACCESS_TOKEN_URL']
    payload = {
        'client_id': app.config['CLIENT_ID'],
        'client_secret': app.config['CLIENT_SECRET'],
        'redirect_uri': app.config['REDIRECT_URI'],
        'code': code
    }
    response = requests.get(token_url, params=payload)
    access_token_data = response.json()
    session['access_token'] = access_token_data['access_token']
    return redirect(url_for('profile.get_profile'))
