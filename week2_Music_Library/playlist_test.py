import unittest
from playlist import Playlist
from song import Song


class TestPlaylist(unittest.TestCase):

    def test_init(self):
        my_playlist = Playlist("My playlist")
        self.assertEqual("My playlist", my_playlist.name)

    def test_add_song_to_an_empty_playlist(self):
        my_playlist = Playlist("My playlist")
        my_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        my_playlist.add_song(my_song)
        self.assertIn(my_song, my_playlist.play_stock)

    def test_add_song_to_a_non_empty_playlist(self):
        my_playlist = Playlist("My playlist")
        first_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        second_song = Song("Ela", "Azis", "Full", 1, 180, 200)
        my_playlist.add_song(first_song)
        my_playlist.add_song(second_song)
        self.assertIn(second_song, my_playlist.play_stock)

    def test_remove_song_from_empty_playlist(self):
        my_playlist = Playlist("My playlist")
        self.assertFalse(my_playlist.remove_song("Ela"))

    def test_remove_song_from_non_empty_playlist(self):
        my_playlist = Playlist("My playlist")
        first_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        second_song = Song("Ela", "Azis", "Full", 1, 180, 200)
        my_playlist.add_song(first_song)
        my_playlist.add_song(second_song)
        my_playlist.remove_song("8-mile")
        self.assertNotIn(first_song, my_playlist.play_stock)

    def test_total_lenght(self):
        my_playlist = Playlist("My playlist")
        first_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        second_song = Song("Ela", "Azis", "Full", 1, 180, 200)
        my_playlist.add_song(first_song)
        my_playlist.add_song(second_song)
        self.assertEqual(360, my_playlist.total_length())

    def test_remove_disrated(self):
        my_playlist = Playlist("My playlist")
        first_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        second_song = Song("Ela", "Azis", "Full", 1, 180, 200)
        my_playlist.add_song(first_song)
        my_playlist.add_song(second_song)
        my_playlist.remove_disrated(3)
        self.assertNotIn(second_song, my_playlist.play_stock)

    def test_remove_bad_quality(self):
        my_playlist = Playlist("My playlist")
        first_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        second_song = Song("Ela", "Azis", "Full", 1, 180, 100)
        my_playlist.add_song(first_song)
        my_playlist.add_song(second_song)
        my_playlist.remove_bad_quality()
        self.assertNotIn(second_song, my_playlist.play_stock)

    '''def test_show_artist(self):
        my_playlist = Playlist("My playlist")
        first_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        second_song = Song("Ela", "Azis", "Full", 1, 180, 100)
        my_playlist.add_song(first_song)
        my_playlist.add_song(second_song)
        self.assertEqual(,my_playlist.show_artist())'''

    def test_str(self):
        my_playlist = Playlist("My playlist")
        first_song = Song("8-mile", "Eminem", "8-mile", 4, 180, 200)
        second_song = Song("Ela", "Azis", "Full", 1, 180, 100)
        my_playlist.add_song(first_song)
        self.assertEqual("Eminem 8-mile - 180", my_playlist.str())

'''import json
import unittest
from playlist import Playlist
from song import Song

test_song1=Song("sd","fa",1,2,3)
test_song2 = Song("dsad",da,2,3)
test_playlist= Playlist("dad")
test.platlist.add_song(test_song1)
test.platlist.add_song(test_song2)
print (test_playlist.__dict__)



if __name__ == '__main__':
    unittest.main()