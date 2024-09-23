import os
from uuid import uuid4
import requests
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = str(uuid4())

# Replace these with your Instagram App's credentials
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = 'https://1302-2406-3003-2001-20aa-4107-5be9-591d-781a.ngrok-free.app/callback'

# Instagram OAuth endpoints
AUTHORIZATION_URL = 'https://api.instagram.com/oauth/authorize'
ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'
GRAPH_API_URL = 'https://graph.instagram.com/me'

SCOPE = 'business_basic,business_content_publish'

# Sample data: An image and the options to choose from
image_url = ""  # Replace with your actual image URL
options = ["Option 1", "Option 2", "Option 3", "Option 4"]


@app.route('/')
def home():
    return render_template('index.html', image_url=image_url, options=options)

@app.route('/login')
def index():
    # Instagram OAuth2 Authorization URL
    auth_url = f'{AUTHORIZATION_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}&response_type=code'
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Instagram redirects back to your app with a 'code' in the query string

    code = request.args.get('code')

    # Exchange the authorization code for an access token
    token_url = ACCESS_TOKEN_URL
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
        'code': code
    }

    response = requests.post(token_url, data=payload)
    access_token_data = response.json()

    # Store the access token in the session (for simplicity)
    session['access_token'] = access_token_data['access_token']

    return redirect(url_for('profile'))

@app.route('/submit_choice', methods=['POST'])
def submit_choice():
    choice = request.form.get('choice')
    # Do something with the choice, e.g., save it to a database
    print(f"User selected: {choice}")
    
    # Redirect back to the main page or a confirmation page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
