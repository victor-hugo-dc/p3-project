# Playlist Manager CLI

This is a command-line interface (CLI) application for managing playlists and songs. The application allows users to create playlists, add songs, edit playlist and song information, and delete playlists or songs. It is built using Python and relies on simple-term-menu for a terminal-based menu interface.
Features

- *Create Playlists*: Users can create a new playlist.
- *List Playlists*: View all created playlists and manage them.
- *Edit Playlists*: Change the name of any playlist.
- *Add Songs*: Add songs to a playlist with a title and artist name.
- *Edit Songs*: Update song titles or artist names.
- *Delete Songs*: Remove songs from a playlist.
- *Delete Playlists*: Delete any playlist.

### Requirements
- Python 3.8+
- Pipenv for managing dependencies

### Setup
1. Clone the repository
```
git clone https://github.com/victor-hugo-dc/p3-project.git
cd p3-project
```
2. Set up the environment: Install Pipenv if it's not already installed:
```
pip install pipenv
```
3. Install dependencies: Run the following command to install the required packages in the Pipenv environment:
```
pipenv install
```
4. Activate the virtual environment: After installing the dependencies, activate the Pipenv shell with:
```
pipenv shell
```
5. Run the application: Once the environment is activated, you can run the application:
```
python lib/cli.py
```

### Usage

When you run the application, you will be presented with the main menu.

Main Menu Options

    Create Playlist: Allows you to create a new playlist by entering its name.
    List All Playlists: Lists all existing playlists. From here, you can:
        Edit Playlist Name
        Delete Playlist
        Add Song to Playlist
        Select a song to edit or delete
    Exit: Closes the application.

Playlist Menu

Once you select a playlist, you will see the following options:

    Edit Playlist Name: Allows you to update the playlist's name.
    Delete Playlist: Removes the playlist.
    Add Song to Playlist: Adds a new song by specifying the song title and artist.
    Select a Song: Lets you choose a song to:
        Edit its title or artist
        Delete the song from the playlist

Song Menu

When a song is selected from the playlist, the following options are available:

    Edit Song Name: Update the song's title.
    Edit Artist Name: Update the artist's name.
    Delete Song: Remove the song from the playlist.