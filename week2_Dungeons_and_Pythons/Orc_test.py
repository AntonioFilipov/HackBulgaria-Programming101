import unittest
from Orc import Orc
from Weapon import Weapon


class TestOrc(unittest.TestCase):

    def test_berserk_factor(self):
        my_orc = Orc("Orc", 80, 1.3)
        self.assertEqual(my_orc.berserk_factor, 1.3)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Orc("Orc", 80, 2.3)

    def test_attack(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.orc.equip_weapon(weapon)
        self.assertEqual(25 * 2, self.orc.attack())

    def test_attack_berserk_without_weapon(self):
        self.assertEqual(0, self.orc.attack())



if __name__ == '__main__':
    unittest.main()
