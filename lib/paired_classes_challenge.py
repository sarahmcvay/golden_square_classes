class Spotifoo:

    def __init__(self):
        self.songs = []

    def add_songs(self, song):
        # we want it to append the songs to the self, the initialised list
        # spotifoo = Spotifoo(self)
        self.songs.append(song)

    def list_songs(self):
        return self.songs
