import unittest
from Hero import Hero


class TestHero(unittest.TestCase):

    def test_known_as(self):
        bron_hero = Hero("Bron", 100, "Broncho")
        self.assertEqual("Bron the Broncho", bron_hero.known_as())

if __name__ == '__main__':
    unittest.main()
