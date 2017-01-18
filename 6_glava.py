# 1
class Thing():
    pass
print(Thing())
ex = Thing()
print(ex)
# 2
class Thing2():
    def __init__(self):
        self.letters = 'abc'
print(Thing2().letters)
# 3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'
print(Thing3().letters)
# 4
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return self.name +' ' + self.symbol + ' ' + str(self.number)
ex1 = Element('Hydrogen', 'H', 1)
# 5
dict1 = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**dict1)
# 6
# hydrogen.dump()
# 7
print(hydrogen)
# 8
class Element1():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def get_name(self):
        return self.__name
ex2 = Element1('Hydrogen', 'H', 1)
print(ex2.get_name())
# 9


class Bear():
    def eats(self):
        return 'berries'


class Rabbit():
    def eats(self):
        return 'clover'


class Octothorpe():
    def eats(self):
        return 'campers'

b = Bear()
r = Rabbit()
o = Octothorpe()
print(b.eats(), r.eats(), o.eats())
# 10


class Laser():
    def does(self):
        return 'disintegrate'


class Claw():
    def does(self):
        return 'crush'


class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self, laser, claw, smartPhone):
        self.laser = laser
        self.claw = claw
        self.smartPhone = smartPhone
    def does(self):
        print(self.laser.does(), self.claw.does(), self.smartPhone.does())

l = Laser()
c = Claw()
s = SmartPhone()
rob = Robot(l, c, s)
rob.does()
