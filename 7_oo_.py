class Person:

    def __init__(self, w, h):
        self.weight = w
        self.height = h

    def __str__(self):
        return "{}/{}".format(self.height,
                              self.weight)

p1 = Person(85, 175)
print(p1)

class SuperPerson(Person):

    def __init__(self, w, h, c):
        Person.__init__(self, w, h)
        self.city = c


print(SuperPerson(85, 170, "Taipei"))







