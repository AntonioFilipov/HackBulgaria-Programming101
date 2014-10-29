import json
from song import Song


class Playlist():
    def __init__(self, name):
        self.name = name
        self.play_stock = []

    def add_song(self, song):
        self.play_stock.append(song)

    def remove_song(self, song_name):
        remover = []
        if self.play_stock == "":
            return False

        for song in self.play_stock:
            if song.title == song_name:
                remover.append(song)

        for removed_song in remover:
            self.play_stock.remove(removed_song)

    def total_length(self):
        length = 0
        for song in self.play_stock:
            length += song.length
        return length

    def remove_disrated(self, rating):
        remover = []
        for song in self.play_stock:
            if song.rating <= rating:
                remover.append(song)

        for removed_song in remover:
            self.play_stock.remove(removed_song)

    def remove_bad_quality(self):
        MIN_BITRATE = 128
        remover = []
        for song in self.play_stock:
            if song.bitrate <= MIN_BITRATE:
                remover.append(song)

        for removed_song in remover:
            self.play_stock.remove(removed_song)

    def show_artist(self):
        artists = set()
        for song in self.play_stock:
            artists.add(song.artist)
        return list(artists)

    def str(self):
        for song in self.play_stock:
            return "{} {} - {}".format(song.artist, song.title, song.length)

    def save(self, file_name):
        song_arr = []
        for song in self.play_stock:
            song_dict = {}
            song_dict["name"] = song.title
            song_dict["author"] = song.artist
            song_arr.append(song_dict)
        my_playlist = {"name": self.name, "songs": song_arr}

        #print (json.dumps(my_playlist))
        filename = "file.json"
        file = open(filename, "w")
        file.write(json.dumps(my_playlist))
        file.close()


    def load(self, file_name):
        filename = "file.json"
        file = open(filename, "r")
        





def main():
    my_playlist = Playlist("My playlist")
    first_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
    second_song = Song("Ela", "Azis", "Full", 1, 180, 100)
    my_playlist.add_song(first_song)
    my_playlist.add_song(second_song)
    #my_playlist.str()
    my_playlist.save("fd")
if __name__ == '__main__':
    main()