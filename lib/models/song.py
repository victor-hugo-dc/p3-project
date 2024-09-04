from . import CURSOR, CONN

class Song:
    all = {}

    def __init__(self, title, artist, playlist_id=None, id=None):
        self.id = id
        self.title = title
        self.artist = artist
        self.playlist_id = playlist_id

    def __repr__(self):
        return f"<Song {self.id}: {self.title} by {self.artist}>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, artist):
        if isinstance(artist, str) and len(artist):
            self._artist = artist
        else:
            raise ValueError("Artist must be a non-empty string")

    @property
    def playlist_id(self):
        return self._playlist_id

    @playlist_id.setter
    def playlist_id(self, playlist_id):
        if isinstance(playlist_id, (int, type(None))):
            self._playlist_id = playlist_id
        else:
            raise ValueError("Playlist ID must be an integer or None")

    @classmethod
    def table_exists(cls):
        """ Check if the table exists """
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='songs';"
        result = CURSOR.execute(sql).fetchone()
        return result is not None

    @classmethod
    def create_table(cls):
        """ Create a new table if it doesn't exist """
        if not cls.table_exists():
            sql = """
                CREATE TABLE songs (
                id INTEGER PRIMARY KEY,
                title TEXT,
                artist TEXT,
                playlist_id INTEGER,
                FOREIGN KEY (playlist_id) REFERENCES playlists (id)
            )
            """
            CURSOR.execute(sql)
            CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table if it exists """
        if cls.table_exists():
            sql = "DROP TABLE IF EXISTS songs;"
            CURSOR.execute(sql)
            CONN.commit()

    def save(self):
        """ Insert or update the song """
        if not self.id:
            sql = "INSERT INTO songs (title, artist, playlist_id) VALUES (?, ?, ?);"
            CURSOR.execute(sql, (self.title, self.artist, self.playlist_id))
            CONN.commit()
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self
        else:
            sql = "UPDATE songs SET title = ?, artist = ?, playlist_id = ? WHERE id = ?;"
            CURSOR.execute(sql, (self.title, self.artist, self.playlist_id, self.id))
            CONN.commit()

    def delete(self):
        """ Delete the song """
        sql = "DELETE FROM songs WHERE id = ?;"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, title, artist, playlist_id=None):
        """ Create and save a new song """
        if not cls.table_exists():
            cls.create_table()
        song = cls(title, artist, playlist_id)
        song.save()
        return song

    @classmethod
    def instance_from_db(cls, row):
        """ Return a Song object from the database row """
        song = cls.all.get(row[0])
        if song:
            song.title = row[1]
            song.artist = row[2]
            song.playlist_id = row[3]
        else:
            song = cls(row[1], row[2], row[3])
            song.id = row[0]
            cls.all[song.id] = song
        return song

    @classmethod
    def get_all(cls):
        """ Get all songs """
        if not cls.table_exists():
            cls.create_table()
        sql = "SELECT * FROM songs;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """ Find a song by ID """
        sql = "SELECT * FROM songs WHERE id = ?;"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """ Find a song by title """
        sql = "SELECT * FROM songs WHERE title = ?;"
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all_titles(cls):
        """ Get titles of all songs """
        songs = cls.get_all()
        return [song.title for song in songs]
