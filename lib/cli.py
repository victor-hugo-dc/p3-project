from simple_term_menu import TerminalMenu
from models.playlist import Playlist
from models.song import Song

CHANGE = 1
CONSTANT = 0

def create_playlist():
    name = input("Enter playlist name: ").strip()
    Playlist.create(name)

def list_playlists():
    menu_items = ["Back"] + [playlist.name for playlist in Playlist.get_all()]
    terminal_menu = TerminalMenu(menu_items, title="Select a Playlist")
    while (choice := terminal_menu.show()) != 0:
        playlist = Playlist.find_by_name(menu_items[choice])
        if playlist_menu(playlist):
            break # the playlist names must be refreshed

def playlist_menu(playlist: Playlist):
    menu_items = ["Back", "Edit Playlist name", "Delete Playlist", "Add Song to Playlist"] + [song.title for song in playlist.songs()]
    terminal_menu = TerminalMenu(menu_items, title = f"Select a Song from {playlist.name}")
    while (choice := terminal_menu.show()) != 0:
        if choice == 1:
            edit_playlist_name(playlist)
            return CHANGE
        
        elif choice == 2:
            return delete_playlist(playlist)
        
        elif choice == 3:
            add_song_to_playlist(playlist)
            return CHANGE
            
        if choice >= 4: 
            song = Song.find_by_title(menu_items[choice])
            song_menu(song)
    
    return CONSTANT

def edit_playlist_name(playlist: Playlist):
    name = input("Enter playlist name: ").strip()
    playlist.name = name
    playlist.save()

def delete_playlist(playlist: Playlist):
    menu_items = ["Yes", "No"]
    terminal_menu = TerminalMenu(menu_items, title = f"Delete {playlist.name}?")
    if terminal_menu.show() == 0:
        playlist.delete()
        return CHANGE
    
    return CONSTANT

def add_song_to_playlist(playlist: Playlist):
    title = input(f"Enter song title for playlist '{playlist.name}': ").strip()
    artist = input(f"Enter artist for song '{title}':").strip()
    Song.create(title, artist, playlist.id)

def song_menu(song: Song):
    menu_items = ["Back", "Edit Song name", "Edit Artist name", "Delete Song from Playlist"]
    terminal_menu = TerminalMenu(menu_items, title = f"{song.title}")
    while (choice := terminal_menu.show()) != 0:
        pass

def main():
    functions: dict = {
        0: create_playlist,
        1: list_playlists,
    }
    
    options: list = [
        "Create Playlist",
        "List All Playlists",
        "Exit"
    ]
    
    terminal_menu = TerminalMenu(options, title = "Main Menu")
    while (choice := terminal_menu.show()) != len(options) - 1:
        functions[choice]()

if __name__ == '__main__':
    main()