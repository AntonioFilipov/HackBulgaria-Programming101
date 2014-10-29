import unittest
from Weapon import Weapon


class TestWeapon(unittest.TestCase):
    def test_init(self):
        my_weapon = Weapon("axe", 30, 0.5)
        self.assertEqual("axe", my_weapon.type_weapon)
        self.assertEqual(30, my_weapon.damage)
        self.assertEqual(0.5, my_weapon.critical_strike_percent)

    def test_set_critical_hit_strike_percent(self):
        with self.assertRaises(ValueError):
            Weapon("axe", 30, 2.3)

    def test_critical_hit(self):
        my_weapon = Weapon("axe", 30, 0.5)
        flags = set()
        for i in range(1000):
            flags.add(my_weapon.critical_hit())
        self.assertEqual(2, len(flags))


if __name__ == '__main__':
    unittest.main()
