from Weapon import Weapon


class Entity():
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.weapon = False

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        if self._MAX_HEALTH < self.health + healing_points:
            self.health = self._MAX_HEALTH
        else:
            self.health += healing_points
        return True

    def has_weapon(self):
        if isinstance(self.weapon, Weapon):
            return True
        return False

    def equip_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon = weapon
        else:
            raise TypeError

    def attack(self):
        if isinstance(self.weapon, Weapon):
            return self.weapon.damage
        else:
            return 0

