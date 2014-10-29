import random
from Orc import Orc
from Hero import Hero


class Fight():
    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def coin_flips(self):
        coin = random.randrange(100)
        if coin < 50:
            return self.hero
        else:
            return self.orc

    def simulate_fight(self):
        attacker = self.coin_flips()
        if attacker == self.orc:
            attacked = self.hero
        else:
            attacked = self.orc

        while self.hero.is_alive() and self.orc.is_alive():
            damage = attacker.attack()
            attacked.take_damage(damage)

            attacked, attacker = attacker, attacked



def main():
    hero = Hero("Gosho", 30, "Goshko")
    orc = Orc("Pesho", 100, 1.3)
    fight = Fight(hero, orc)
if __name__ == '__main__':
    main()
