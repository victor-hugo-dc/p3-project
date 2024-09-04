from . import CURSOR, CONN
from .song import Song

class Playlist:
    all = {}

    def __init__(self, name: str, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @classmethod
    def table_exists(cls):
        """ Check if the table exists """
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='playlists';"
        result = CURSOR.execute(sql).fetchone()
        return result is not None

    @classmethod
    def create_table(cls):
        """ Create a new table if it doesn't exist """
        if not cls.table_exists():
            sql = """
                CREATE TABLE playlists (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
            """
            CURSOR.execute(sql)
            CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table if it exists """
        if cls.table_exists():
            sql = "DROP TABLE IF EXISTS playlists;"
            CURSOR.execute(sql)
            CONN.commit()

    def save(self):
        """ Insert or update the playlist """
        if not self.id:
            sql = "INSERT INTO playlists (name) VALUES (?);"
            CURSOR.execute(sql, (self.name,))
            CONN.commit()
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self
        else:
            sql = "UPDATE playlists SET name = ? WHERE id = ?;"
            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()

    def delete(self):
        """ Delete the playlist """
        sql = "DELETE FROM playlists WHERE id = ?;"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name):
        """ Create and save a new playlist """
        playlist = cls(name)
        playlist.save()
        return playlist

    @classmethod
    def instance_from_db(cls, row):
        """ Return a Playlist object from the database row """
        playlist = cls.all.get(row[0])
        if playlist:
            playlist.name = row[1]
        else:
            playlist = cls(row[1])
            playlist.id = row[0]
            cls.all[playlist.id] = playlist
        return playlist

    @classmethod
    def get_all(cls):
        """ Get all playlists """
        if not cls.table_exists():
            cls.create_table()
        sql = "SELECT * FROM playlists;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """ Find a playlist by ID """
        sql = "SELECT * FROM playlists WHERE id = ?;"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """ Find a playlist by name """
        sql = "SELECT * FROM playlists WHERE name = ?;"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def songs(self):
        """ Retrieve all songs in this playlist """
        try:
            sql = "SELECT * FROM songs WHERE playlist_id = ?;"
            rows = CURSOR.execute(sql, (self.id,)).fetchall()
            return [Song.instance_from_db(row) for row in rows]
        except:
            return []
    
    @classmethod
    def get_all_names(cls):
        """ Get names of all playlists """
        playlists = cls.get_all()
        return [playlist.name for playlist in playlists]