"""This file contains constants mostly called by utils.py
"""
# List of current supported service by SoCo
SUPPORTED_SERVICES = ["Amazon Music", "Apple Music", "Deezer",
                      "Google Play Music", "Music Library", "Napster", "Plex",
                      "SoundCloud", "Spotify", "TuneIn", "Wolfgangs Music",
                      "YouTube Music"]

# Service that requires authentication
REQUIRED_AUTHENTICATION = ['Spotify', 'Amazon Music']

# List a supported categories for MusicLibrary
SUPPORTED_LIBRARY_CATEGORIES = ['artists', 'album_artists', 'albums',
                                'genres', 'composers', 'tracks', 'share',
                                'sonos_playlists', 'playlists']

# Token file used by SoCo Python library
TOKEN_FILE = '/.config/SoCo/token_store.json'

# Volume values
DEFAULT_VOL_INCREMENT = 10
LOUDER_QUIETER = 30

# Link to the URL shortener
URL_SHORTENER = 'https://sonos.smartgic.io/create'
