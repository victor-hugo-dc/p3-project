from simple_term_menu import TerminalMenu


def main():
    options = [
        "Create Playlist",
        "List All Playlists",
        "Edit Playlist Name",
        "Delete Playlist",
        "Add Song to Playlist",
        "Delete Song from Playlist",
        "Exit"
    ]
    
    while True:
        terminal_menu = TerminalMenu(options, title="Main Menu")
        choice_index = terminal_menu.show()

        if choice_index == 0:
            # create_playlist()
            pass
        elif choice_index == 1:
            # list_playlists()
            pass
        elif choice_index == 2:
            # edit_playlist_name()
            pass
        elif choice_index == 3:
            # delete_playlist()
            pass
        elif choice_index == 4:
            # add_song_to_playlist()
            pass
        elif choice_index == 5:
            # delete_song_from_playlist()
            pass
        elif choice_index == 6:
            break

if __name__ == '__main__':
    main()