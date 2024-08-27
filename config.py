import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    # General Flask Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False

    # Spotify API Config
    SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')
