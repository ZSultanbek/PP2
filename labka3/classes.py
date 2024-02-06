#1_________
print("#1__________________")
class CAPSLOCK:
    getString = input()

    printString = print(getString.upper())

line = CAPSLOCK()
line.getString
line.printString

#2__________________
print("#2_______________")
class Shape:
    def __init__(self, area=None):
        if area is None:
            area = 0
        self.area = area
    
    def Area(self):
        print(self.area)


class Square(Shape):
    def __init__(self, area=None, length=None):
        super().__init__(area)
        if length is None:
            length = 0
        self.length = length

someshape = Shape()
someshape.area = 10
someshape.Area()

somesquare = Square()
somesquare.area = 9
somesquare.Area()
somesquare.length = 3
print (somesquare.length, "Length of square with area 9")

print("#3____________________")
#3___________________________
class Rectangle(Shape):
    def __init__(self, area, length=None, width=None):
        super().__init__(area)
        if length == None:
            length = 0
        if width == None:
            width = 0
        self.length = length
        self.width = width
        area = length*width
        self.area = area
    
    def Area(self):
        print(self.area, self.length, self.width)

somerec = Rectangle(10, 5, 2)
somerec.length = 5
somerec.width = 2
somerec.Area()

print("#4_______________")
#4______________________

class Point():
    def __init__(self, x=None, y=None):
        if x == None:
            x = 0
        if y == None:
            y = 0
        self.x = x
        self.y = y


    def show(self):
        print (self.x, self.y)

    def move(self, nx, ny):
        self.x = nx
        self.y = ny

    def dist(x2, y2, self):
        avrx = x2 - self.x
        avry = y2 - self.y
        d = (avrx**2 + avry**2)**0.5
        return d
    def dist(point, self):
        avrx = point.x - self.x
        avry = point.y - self.y
        d = (avrx**2 + avry**2)**0.5
        return d
    
p1 = Point(-1, -1)
p2 = Point(2, 1)
p1.show()
p1.move(1, 1)
p1.show()
print (p1.dist(p2))

print("#5______________")
#5_____________________
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        money = int(input("gimme money: "))
        self.balance += money
    
    def withdraw(self):
        take = int(input("how much you steal: "))
        if take > self.balance:
            print("Nah, too much")
        else:
            self.balance -= take
            return self.balance
MyBank = Account("Kelgenbaev", 1000000)    
print(MyBank.balance)
MyBank.deposit()
print(MyBank.balance)
MyBank.withdraw()
print(MyBank.balance, ", tenge you have")

print("#6___________")
#6_____________________

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def IsPrime(num):
    for i in range (2, num):
        if num%i == 0:
            return False
        
    return True

filter = lambda a: IsPrime(a)
newlist = [i for i in list if filter(i) == False]
print(newlist)
