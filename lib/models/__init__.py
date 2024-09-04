import sqlite3

CONN = sqlite3.connect('playlists.db')
CURSOR = CONN.cursor()