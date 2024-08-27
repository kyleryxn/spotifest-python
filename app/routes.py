import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import render_template, redirect, url_for, request
from app import app
from datetime import datetime, timedelta

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope='user-top-read'
))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    # Redirect to Spotify authentication page
    auth_url = sp.auth_manager.get_authorize_url()
    return redirect(auth_url)


@app.route('/callback')
def callback():
    # Handle the redirect from Spotify after authentication
    code = request.args.get('code')
    sp.auth_manager.get_access_token(code)
    return redirect(url_for('top_artists'))


@app.route('/top-artists')
def top_artists():
    # Calculate the dates for Friday, Saturday, and Sunday
    today = datetime.today()
    friday = today + timedelta((4 - today.weekday()) % 7)
    saturday = friday + timedelta(days=1)
    sunday = friday + timedelta(days=2)

    # Fetch current user's username
    user_profile = sp.current_user()
    user_name = user_profile['display_name']

    # Fetch the user's top 50 artists from Spotify
    results = sp.current_user_top_artists(limit=50, time_range='long_term')
    artists = [artist['name'] for artist in results['items']]

    # Pass the dates and artists to the template
    return render_template(
        'lineup.html',
        user_name=user_name,
        artists=artists,
        friday=friday.strftime('%B %d'),
        saturday=saturday.strftime('%B %d'),
        sunday=sunday.strftime('%B %d')
    )


@app.route('/logout')
def logout():
    # Clear session or perform logout logic if needed
    return redirect(url_for('home'))
