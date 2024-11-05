from flask import Flask, redirect, request, session, url_for
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

# Set a random secret key for session management in Flask
app.secret_key = os.getenv("FLASK_SECRET_KEY", "your-default-secret-key")

# Spotify API credentials from environment variables
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# SpotifyOAuth setup with environment variables
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-library-read streaming"
)

@app.route("/")
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route("/callback")
def callback():
    session.clear()
    code = request.args.get("code")
    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = token_info
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    token_info = session.get("token_info", None)
    if token_info:
        sp = spotipy.Spotify(auth=token_info["access_token"])
        user_profile = sp.current_user()
        return f"Hello, {user_profile['display_name']}! You are now authenticated."
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(port=5000)
