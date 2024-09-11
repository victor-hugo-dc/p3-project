from simple_term_menu import TerminalMenu
from models.playlist import Playlist
from models.song import Song

def create_playlist():
    name = input("Enter playlist name: ").strip()
    Playlist.create(name)

def list_playlists():
    menu_items = ["Back"] + [playlist.name for playlist in Playlist.get_all()]
    terminal_menu = TerminalMenu(menu_items, title="Select a Playlist")
    while (choice := terminal_menu.show()) != 0:
        playlist = Playlist.find_by_name(menu_items[choice])
        playlist_menu(playlist)

def playlist_menu(playlist: Playlist):
    menu_items = ["Back", "Edit Playlist name", "Delete Playlist", "Add Song to Playlist"] + [song.title for song in playlist.songs()]
    terminal_menu = TerminalMenu(menu_items, title = f"Select a Song from {playlist.name}")
    while (choice := terminal_menu.show()) != 0:
        if choice >= 4: 
            song = Song.find_by_title(menu_items[choice])
            song_menu(song)

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