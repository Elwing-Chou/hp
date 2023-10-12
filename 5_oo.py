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

# 當你頻繁的需要使用某種東西->定義型態
class Person:

    def __init__(self, h, w):
        self.height = h
        self.weight = w

    def cbmi(self):
        bmi = self.weight / (self.height / 100) ** 2
        return bmi

# 一個形態可以具備什麼東西? 1. 專屬功能(method)  2. 專屬值(attributes)
p1 = Person(175, 80)
print(p1.cbmi())

p2 = Person(180, 70)
print(p2.cbmi())






