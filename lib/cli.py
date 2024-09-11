from simple_term_menu import TerminalMenu
from models.playlist import Playlist

def create_playlist():
    name = input("Enter playlist name: ").strip()
    Playlist.create(name)

def list_playlists():
    menu_items = ["Back"] + [playlist.name for playlist in Playlist.get_all()]
    terminal_menu = TerminalMenu(menu_items, title="Select a Playlist")
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