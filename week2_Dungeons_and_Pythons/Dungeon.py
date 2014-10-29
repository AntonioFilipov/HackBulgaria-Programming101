import sys
from Hero import Hero
from Orc import Orc


class Dungeon():

    def __init__(self, filepath):
        self.filepath = filepath

    def print_map(self):
        file = open(self.filepath, "r")
        content = file.read()
        print (content)
        file.close()

    def spawn(self, player_name, entity):
        file = open(self.filepath, "r")
        content = file.read()
        file.close()
        file = open(self.filepath, "w")
        if isinstance(entity, Hero):
            content = content.replace("S", "H", 1)
        elif isinstance(entity, Orc):
            content = content.replace("S", "O", 1)
        file.write("".join(content))
        file.close()

def main():
    my_map = Dungeon("basic_dungeon.txt")
    my_map.print_map()
    bron_hero = Hero("Bron", 100, "Broncho")
    my_orc = Orc("Orc", 80, 1.3)
    my_map.spawn("fdsfd", bron_hero)
    my_map.print_map()

if __name__ == '__main__':
    main()


