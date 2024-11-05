import os

# Fetch the credentials from environment variables to keep them secure
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "!"  # You can change this to your preferred command prefix

# Spotify API credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
