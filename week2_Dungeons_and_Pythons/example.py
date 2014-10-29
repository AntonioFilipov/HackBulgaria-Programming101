class Person:
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name

    def name(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Doctor(Person):
    def name(self):
        return "{0}, M.D.".format(Person.name(self))

print(Doctor("Gregory", "House").name()) # Gregory House, M.D.