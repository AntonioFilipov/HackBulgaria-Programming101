import unittest
from Dungeon import Dungeon
from Hero import Hero
from Orc import Orc

class TestDungeon(unittest.TestCase):

    def test_init(self):
        my_map = Dungeon("basic_dungeon.txt")
        self.assertEqual("basic_dungeon.txt", my_map.filepath)

    def test_spawn(self):
        my_map = Dungeon("basic_dungeon.txt")
        bron_hero = Hero("Bron", 100, "Broncho")
        my_orc = Orc("Orc", 80, 1.3)
        

if __name__ == '__main__':
    unittest.main()