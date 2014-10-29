class Song():
    MAX_RATING = 5
    MIN_RAING = 1

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rate):
        if rate > Song.MAX_RATING or rate < Song.MIN_RAING:
            raise ValueError("Rating out of range {} - {}".format(Song.MIN_RAING, Song.MAX_RATING))
        else:
            self.rating = rate
