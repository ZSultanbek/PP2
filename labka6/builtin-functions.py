#1________________________
print("#1_________________")
def multiply_list_el(list):
    result = 1
    for i in list:
        result = eval("i * result")
        
    return result

l = [3, 3, 2, 1]
print(multiply_list_el(l))


#2________________________
print("#2_________________")
def upper_and_lower(st):
    countUp = 0
    countDown = 0
    for i in st:
        if i.isupper():
            countUp+=1
        elif i.islower():
            countDown+=1
    return [countUp, countDown]      
ex2 = "lalaLALA192830, HeavyDirtySould"
print("{0} upcase letters, {1} lowcase letters".format(upper_and_lower(ex2)[0], upper_and_lower(ex2)[1]))

#3________________________
print("#3_________________")
def ispali(st):
    st.lower()
    listrev = list(st)
    listrev.reverse()
    listor = list(st)
    return listor == listrev
ex3 = "pneumonoultramicroscopicsilicovolcanoconiosis"
ex33 = "aibohphobia"
print(eval("ispali(ex3)"))
print(eval("ispali(ex33)"))

#4________________________
print("#4_________________")
import time
def sqrtof(num):
    return num**0.5

num = float(input())
ms = float(input())
ms /= 1000
time.sleep(ms)
print(eval("sqrtof(num)"))


#5________________________
print("#5_________________")
def is_all_true(tup):
    for i in tup:
        if i == False:
            return False
    return True

ex5 = (1, True, -10, [0])
ex55 = (1, True, -10, [1], "")
ex555 = (1, True, 0, [])
print(eval("is_all_true(ex5)"))
print(eval("is_all_true(ex55)"))
print(eval("is_all_true(ex555)"))
