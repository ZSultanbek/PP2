import math



#1________________________________
print("#1_________________________")

def deg_to_rad(degree):
    rads = degree * (math.pi / 180.0)

    return rads

print(deg_to_rad(15))



#2________________________________
print("#2_________________________")    

def trapez_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
print(trapez_area(base1, base2, height))

#3________________________________
print("#3_________________________")

def regular_polygon_area(num, length):
    return (1/4) * num * length**2 / math.tan(math.pi / num)

num = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
print(regular_polygon_area(num, length))


#4________________________________
print("#4_________________________")

def parallelogram_area(a, b):
    return a * b

a = int(input("Length of base: "))
b = int(input("Height of parallelogram: "))
print(parallelogram_area(a, b))
