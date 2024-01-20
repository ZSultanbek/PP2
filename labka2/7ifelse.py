a = 100
t = 42
if a > t:
    print ("Level of concern =", a)

if a != t:
    print ("Level of concern =", "not equal")

if a == t:
    print ("Level of concern =", a + t)
else:
    print (a, t)


if a == t:
    print ("Level of concern =", a + t)
elif a > t:
    print (a)
else:
    print (t)

a = 1
b = 2
c = 1.3
d = 1.3

if a == b and c == d:
    print("Hello")
if a == b or c == d:
    print("Hello")


if c > a:
    print ("YESESSSSSSSSSSSE")

print ("A") if a > b else print ("nah B")

if a == d or c == d:
    print ("DIC")
