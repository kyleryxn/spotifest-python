import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the paths to the templates and static directories
template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

# Initialize the Flask app with custom template and static folder paths
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Example: Setting up a config variable (optional)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from app import routes
