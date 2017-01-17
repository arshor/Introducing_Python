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
        return self.name + self.symbol + str(self.number)
ex1 = Element('Hydrogen', 'H', 1)
# 5
dict1 = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**dict1)
# 6
# hydrogen.dump()
# 7
print(hydrogen)




