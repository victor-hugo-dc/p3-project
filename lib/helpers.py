from models.playlist import Playlist

def list_all_playlists():
    playlists = Playlist.get_all()
    return [repr(playlist) for playlist in playlists], playlists

def list_all_songs(playlist):
    songs = playlist.songs()
    return [repr(song) for song in songs], songs