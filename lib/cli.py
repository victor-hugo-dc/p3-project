from simple_term_menu import TerminalMenu
from helpers import create_playlist, list_playlists

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