import unittest
from song import Song


class TestSong(unittest.TestCase):

    def test_init(self):
        my_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        self.assertEqual("8-mile", my_song.title)
        self.assertEqual("Eminem", my_song.artist)
        self.assertEqual("8-mile", my_song.album)
        self.assertEqual(4, my_song.rating)
        self.assertEqual(180, my_song.length)
        self.assertEqual(200, my_song.bitrate)

    def test_rate_in(self):
        my_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        my_song.rate(2)
        self.assertEqual(2, my_song.rating)

    def test_rate_out(self):
        my_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        with self.assertRaises(ValueError):
            my_song.rate(200)


if __name__ == '__main__':
    unittest.main()
