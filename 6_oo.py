# 當你某幾句重複寫->定義函式
def add(n1, n2):
    new = n1 + n2
    return new

print(add(3, 2))
print(add([1, 2], [3,4]))

# 當你頻繁的需要使用某種東西->定義型態
class Person:
    pass

# 一個形態可以具備什麼東西? 1. 專屬功能(method)  2. 專屬值(attributes)
p1 = Person()
p1.height = 175
p1.weight = 80

bmi = p1.weight / (p1.height / 100) ** 2

# __: Google Python Data model
# 當你頻繁的需要使用某種東西->定義型態
class Person:

    def __init__(self, h, w):
        self.height = h
        self.weight = w

    def cbmi(self):
        bmi = self.weight / (self.height / 100) ** 2
        return bmi

    def __str__(self):
        return "[height]:{} [weight]:{}".format(self.height,
                                                self.weight)
    def __int__(self):
        return int(self.cbmi())

    def __add__(self, other):
        newh = (self.height + other.height) / 2
        neww = (self.weight + other.weight) / 2
        return Person(newh, neww)

# 一個形態可以具備什麼東西? 1. 專屬功能(method)  2. 專屬值(attributes)
p1 = Person(175, 80)
print(p1.cbmi())

p2 = Person(180, 70)
print(p2.cbmi())

# str(p1) -> p1.__str__()
print(p1)

# p1.__add__(p2)
print(p1 + p2)

# p1.__int__()
print(int(p1))




