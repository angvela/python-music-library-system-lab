class Song:
    """A class representing a song in the music library.

    The class keeps track of all created instances and exposes
    various helpers for querying the library state.  Tests depend on
    several class attributes so they're explicitly initialized here.
    """

    # class attributes used by the tests
    count = 0
    all_songs = []
    artists = set()
    genres = set()
    artist_count = {}
    genre_count = {}
    songs_by_artist = {}
    songs_by_genre = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # maintain global song list and counters
        Song.all_songs.append(self)
        Song.count += 1

        # track artists
        Song.artists.add(artist)
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
        Song.songs_by_artist.setdefault(artist, []).append(self)

        # track genres
        Song.genres.add(genre)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.songs_by_genre.setdefault(genre, []).append(self)

    # the helpers from earlier tests / expected in library
    @classmethod
    def reset_library(cls):
        """Reset all class-level state (useful between tests)."""
        cls.count = 0
        cls.all_songs = []
        cls.artists = set()
        cls.genres = set()
        cls.artist_count = {}
        cls.genre_count = {}
        cls.songs_by_artist = {}
        cls.songs_by_genre = {}

    @classmethod
    def get_all_songs(cls):
        """Return a list of tuples (name, artist, genre) for every song."""
        return [(s.name, s.artist, s.genre) for s in cls.all_songs]

    @classmethod
    def get_unique_artists(cls):
        """Return a list of all unique artists in the library."""
        return list(cls.artists)

    @classmethod
    def get_unique_genres(cls):
        """Return a list of all unique genres in the library."""
        return list(cls.genres)
