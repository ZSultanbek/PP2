#1________________________________
print("#1_________________________")
def squareupgen(n):
    for i in range(0,n+1):
        yield i**2

for sqaure in squareupgen(10):
    print (sqaure, end=" ")


print("")
#2________________________________
print("#2_________________________")
n = int(input())
def ComeSepgen(n):
    for i in range(0, n+1):
        if i%2==0:
            yield i

for num in ComeSepgen(n):
    print(num, end=",")


print("")
#3________________________________
print("#3_________________________")
def IsDivgen(n):
    for i in range(0, n+1):
        if i%3==0 and i%4==0:
            yield i

def printOut(n):
    for num in IsDivgen(n):
        print(num, end=" ")

printOut(24)

print("")
#4________________________________
print("#4_________________________")
def squaregen(a, b):
    for i in range(a,b+1):
        yield i**2

for sqaure in squaregen(5, 15):
    print (sqaure, end=" ")


print("")
#5________________________________
print("#5_________________________")
def DownTowngen(n):
    i = n
    while i >= 0:
        yield i
        i-=1

n = 20
for num in DownTowngen(n):
    print (num, end=" ")


