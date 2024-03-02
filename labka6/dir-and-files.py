import os

#1___________________
print("#1____________")
path = r"C:\Users\zhani\OneDrive\Рабочий стол\pp2"
lstofpath = os.listdir(path)
onlydir = [i for i in lstofpath if os.path.isdir(os.path.join(path, i))]
onlyfile = [i for i in lstofpath if os.path.isfile(os.path.join(path, i))]
print(onlydir)
print(onlyfile)
print(lstofpath)


#2___________________
print("#2____________")
print("Such file exists:", os.access(r"C:\Users\zhani\OneDrive\Рабочий стол\pp2", os.F_OK))
print("Such file is readable:", os.access(r"C:\Users\zhani\OneDrive\Рабочий стол\pp2", os.R_OK))
print("Such file is writeable:", os.access(r"C:\Users\zhani\OneDrive\Рабочий стол\pp2", os.W_OK))
print("Such file is executable:", os.access(r"C:\Users\zhani\OneDrive\Рабочий стол\pp2", os.X_OK))


#3___________________
print("#3____________")
testpath = r"C:\Users\zhani\OneDrive\Рабочий стол\pp420"
if os.path.exists(testpath):
    print(os.path.basename(testpath))
    print(os.path.dirname(testpath))
else:
    print("Such path doesn't exists")


#4___________________
print("#4____________")
#reading lines of test2.txt
test2path = open(r"labka6\test2.txt", "r")
print("We have {0} lines".format(len(test2path.readlines())))
test2path.close()





#5___________________
print("#5____________")
#writing list to test3.txt
lst = ["some list i guess", 0, 1, True]
file3 = open(r"labka6\test3.txt", "a")
file3.write(str(lst)+"\n")
file3.close()
print("File successfully changed")




#6___________________
print("#6____________")
froma = ord("A")
toz = ord("Z")

#delete existing files
for i in range (froma, toz+1):
    if os.path.exists(r"labka6\AtoZ files\{0}.txt".format(chr(i))):
        os.remove(r"labka6\AtoZ files\{0}.txt".format(chr(i)))

#creating new files
for i in range (froma, toz+1):
    fileAZ = open(r"labka6\AtoZ files\{0}.txt".format(chr(i)), "x")

fileAZ.close()
path1 = r"C:\Users\zhani\OneDrive\Рабочий стол\pp2\labka6\AtoZ files"
allpaths = os.listdir(path1)
files = [i for i in allpaths if os.path.isfile(os.path.join(path1, i))]
print(files)


#7___________________
print("#7____________")
firstfile = open(r"labka6\test3.txt", "r")
secondfile = open(r"labka6\AtoZ files\A.txt", "w+")

secondfile.write(firstfile.read())
firstfile.close()
secondfile.close()

#printing the result of A.txt
secondfile = open(r"labka6\AtoZ files\A.txt", "r")
strsecond = secondfile.read()
print(strsecond)
secondfile.close()


#8___________________
print("#8____________")
deletethis = r"labka6\AtoZ files\Z.txt"

#checking if exists
if os.path.exists(deletethis):
    #chicking if has access
    if os.access(r"C:\Users\zhani\OneDrive\Рабочий стол\pp2", os.F_OK):
        #deleting the file
        os.remove(deletethis)
        print("file {0} is deleted".format(deletethis))

