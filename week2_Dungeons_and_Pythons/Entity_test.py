import unittest
from Entity import Entity
from Weapon import Weapon


class TestEntity(unittest.TestCase):

    def test_init(self):
        my_entity = Entity("Furious", 100)
        self.assertEqual("Furious", my_entity.name)
        self.assertEqual(100, my_entity.health)

    def test_get_health(self):
        my_entity = Entity("Furious", 100)
        self.assertEqual(100, my_entity.get_health())

    def test_is_alive(self):
        my_entity = Entity("Furious", 100)
        my_entity.health = 0
        self.assertFalse(my_entity.is_alive())

    def test_take_damage(self):
        my_entity = Entity("Furious", 100)
        my_entity.take_damage(30)
        self.assertEqual(70, my_entity.get_health())

    def test_take_healing(self):
        my_entity = Entity("Furious", 100)
        my_entity.health = 50
        heal_result = my_entity.take_healing(20)
        self.assertEqual(70, my_entity.get_health())
        self.assertTrue(heal_result)

    def test_take_healing_dead(self):
        my_entity = Entity("Furious", 100,)
        my_entity.health = 0
        heal_result = my_entity.take_healing(20)
        self.assertEqual(0, my_entity.get_health())
        self.assertFalse(heal_result)

    def test_take_healing_maximum_health(self):
        my_entity = Entity("Furious", 100)
        my_entity.health = 70
        heal_result = my_entity.take_healing(40)
        self.assertEqual(100, my_entity.get_health())
        self.assertTrue(heal_result)

    def test_has_weapon(self):
        my_weapon = Weapon("axe", 30, 0.5)
        my_entity = Entity("Furious", 100)
        my_entity.equip_weapon(my_weapon)
        self.assertTrue(my_entity.has_weapon())
        my_entity = Entity("Furious", 100)
        self.assertFalse(my_entity.has_weapon())

    def test_attack_without_weapon(self):
        my_entity = Entity("Furious", 100)
        self.assertEqual(0, my_entity.attack())

    def test_attack_with_weapon(self):
        my_entity = Entity("Furious", 100)
        my_weapon = Weapon("axe", 30, 0.5)
        my_entity.equip_weapon(my_weapon)
        self.assertEqual(30, my_entity.attack())

if __name__ == '__main__':
    unittest.main()
