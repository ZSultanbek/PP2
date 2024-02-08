import random


print("#1______")
#1________________________________
def ConvertToOunce(grams):
    ounces = 28.3495231 * grams
    return ounces
grams = 32
print (ConvertToOunce(grams))


print("#2______")
#2________________________________
def ConvertToCelcius(far):
    cel = ((5 / 9) * (far - 32))
    return cel
far = 100
print (ConvertToCelcius(far))


print("#3______")
#3________________________________
def solve(numheads, numlegs):
    rabb = (numlegs - 2*numheads)/2
    chick = numheads-rabb
    return [chick, rabb]
a = 35
b = 94
print (solve(a, b))


print("#4______")
#4________________________________
def isprime(num):
    for i in range(1, num+1):
        if num%i == 0 and i != 1 and i != num:
            return False
    return True

def filter_prime(nums):
    filteredlist = []
    for i in nums:
        if isprime(i) and i != 1:
            filteredlist.append(i)
    return filteredlist

print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print("#5______")
#5_________________________________________
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

def nextpermutation(string):
    string = sorted(string)
    perms = []
    stemp = string
    i = len(string)-1
    j = len(string)-2
    counter = -1
    minic = 0
    while i > 0:
        counter += 1
        if counter >= factorial(len(string)):
            break

        if j >= len(string) or j < ((-1) * len(string)):
            j = len(string)-2
        stemp[j], stemp[i] = stemp[i], stemp[j]
        j -= 1
        minic += 1

        if stemp not in perms:
            perms = stemp
            print(perms, counter)
            continue

        if j+minic != i and minic > 4:
            j = i-1
                
    return perms
string = ["4", "4", "1", "0"]
print (string)
string = nextpermutation(string)
'''
012
021
120
102
201
210
'''

print("#6______")
#6______________________________
def reversestr(string):
    words = string.split(' ')
    answer = ""
    for w in range (len(words)-1, -1, -1):
        answer += words[w]+' '
    return answer
print (reversestr("Hi MOm"))

print("#7______")
#7_________________________________
def has_33(nums):
    for i in range(len(nums)):
        nums[i] = str(nums[i])

    snums = " ".join(nums)

    if "3 3" in snums:
        return True
    else:
        return False
print (has_33([1, 3, 3]))
print (has_33([1, 3, 1, 3]))
print (has_33([3, 1, 3]))

print("#8______")
#8_________________________________
def spy_game(nums):
    agent007 = [False, False, False]
    indexes = []
    for i in range (0, 2):
        if 0 in nums:
            indexes.append(nums.index(0))
            nums[nums.index(0)] = 1
            agent007[i] = True
    if 7 in nums:
        indexes.append(nums.index(7))
    if indexes == sorted(indexes) and len(indexes) == 3:
        return True 
    
    return False
print (spy_game([1, 2, 4, 0, 0, 7, 5]))
print (spy_game([1,0,2,4,0,5,7]))
print (spy_game([1,7,2,0,4,5,0]))



print("#9______")
#9__________________________
def VolumeOfSphere(radius):
    volume = (4.0/3.0) * 3.14159 * radius
    return volume
print (VolumeOfSphere(4))


print("#10______")
#10_____________________
def UniqueList(list):
    YeahList = []
    for i in list:
        if i not in YeahList:
            YeahList.append(i)

    return YeahList
print (UniqueList([0, 0, 10, 0, 2, 0 ]))



print("#11_____")
#11__________________
def IsPali(string):
    list = []
    string = string.lower()
    for i in string:
        if i not in " ,.!?/[]();:'":
            list.append(i)
    list2 = list.copy()
    list2.reverse()
    return list == list2 
print(IsPali("HI MOM"))
print(IsPali("RACEcar"))


print("#12_________")
#12_________________
def histogram(list):
    for i in list:
        for j in range (0, i):
            print("*", end="")
        print("")
histogram([4, 9, 7])

print("#13______________")
#13___________________

name = input("Hello! What is your name?\n")

guess = int(input("Well, {0}, I am thinking of a number between 1 and 20.\nTake a guess.\n".format(name)))

number = random.randrange(1, 21)
counter = 1
while guess != number:
    if guess > number:
        print("Your guess is too high.")
    if number > guess:
        print("Your guess is too low.")
    guess = int(input("Take a guess.\n"))
    counter+= 1

print ("Good job, {0}! You guessed my number in {1} guesses!".format(name, counter))
