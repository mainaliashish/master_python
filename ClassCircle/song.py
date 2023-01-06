class Song:
    """
    Class to represent a Song
    Attributes:
        title(str) : The title of the song.
        artist(Artist) : The artist object representing song creator.
        duration(int) : The duration of the song in second. May be Zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    Class to represent an Album, using its track list
    Attributes:
        album_name(str) : The name of the album.
        year(int) : The year the album was released.
        artist: (Artist) : The artist responsible for album.
                        If not specified the artist will default to an artist with name "Various Artist"
        tracks: (List[Song]) : A list of songs in the album
    Methods:
        addSong: used to add a song in the album's track list.
    """

    def __init__(self, album_name, year, artist=None):
        self.album_name = album_name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist
        self.track = []

    def add_song(self, song, position=None):
        """
        Add a song to the track list
        Args:
        :param song: Expects string. A song to add.
        :param position: Expects integer. If specified, the song will be added to the position in the
                        track list. inserting song in between the songs.
        :return:
        """
        if position is None:
            self.track.append(song)
        else:
            self.track.index(position, song)


class Artist:
    """
    basic class to store artist details
    Attributes:
        name(str) : The name of the artist
        album(List[Album]) : A list of the album by the artist.
                    This list only includes those albums in the collection, it is not an
                    exhaustive lists of the artist's published albums.
    Methods:
        add_album: Used to add a new album to the artist lists.
    """

    def __init__(self, name):
        self.name = name
        self.album = []

    def add_album(self, album):
        """
        Add a new album to the list
        Args:
            album(Album) : Album object to the list
                        If the album is already present, it will not be added.
        """
        self.album.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            """
             data row should consist of (artist, album, year, song)
            """
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist == None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                 # we've just read details for new artist
                 # store the current artist in the current artist collection then create new artist object
                new_artist.add_album(new_album)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.album_name != album_field:
                # we've just read a new album for the current artist
                # store the current album in the current artist collection then create new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new song object and add it to current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After reading a last line of text file, we will have artist and album that have not been stored
        # so, process it now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    return artist_list


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))
