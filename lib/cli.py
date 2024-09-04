from simple_term_menu import TerminalMenu

terminal_menu = TerminalMenu([
    "Create Playlist",
    "List All Playlists",
    "Edit Playlist Name",
    "Delete Playlist",
    "Add Song to Playlist",
    "Delete Song from Playlist",
    "Search Songs",
    "Exit"
])
choice_index = terminal_menu.show()