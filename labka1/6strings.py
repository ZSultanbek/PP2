abc = "   DEFghijklmnOPqrstuvwxyz "
print (len(abc))

print (abc[0] + " first char of abc")
print (abc[2:5])
print (abc.strip())
print (abc.upper())
print (abc.lower())
print (abc.replace("DEF", "DEFUC"))

howold = 32054718
nonotfalse = "I am certainly {} years old, yea"
print (nonotfalse.format(howold))
