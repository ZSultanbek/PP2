import re
text = open(r"labka5\raw.txt", encoding="utf8")
txt = " ".join((str(text.read())).split("\n"))
txt1 = txt

#1________________________________
print("1______________________")
abb1 = re.findall("ab*", txt)
print(abb1)

#2________________________________
print("2______________________")
abb2 = re.findall("a{1}b{2,3}", txt)
print(abb2)


#3________________________________
print("3______________________")
lowunder = re.findall(r"^[a-z]+_[a-z]+$", txt)
print(lowunder)


#4________________________________
print("4______________________")
upplow = re.findall("[A-Z][a-z]+", txt)
print(upplow)

#5________________________________
print("5______________________")
a_b = re.findall(r"a.*b$", txt)
print(a_b)

#6________________________________
print("6______________________")
def ReplaceWithColon(input_string):
    return re.sub("[ ,.]", ":", input_string)
txt = ReplaceWithColon(txt)
print(txt)

#7________________________________
print("7______________________")
def Snake_case_toCamelCase(snake_case):
    words = snake_case.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])
txt = Snake_case_toCamelCase(txt)
print(txt)

#8________________________________
print("8______________________")
def SplitAtUppercase(input_string):
    return re.split(r'(?=[A-Z])', input_string)
txt = SplitAtUppercase(txt)
txt = " ".join(txt)
print(txt)
#9________________________________
print("9______________________")
def InsertSpacesAtCaps(input_string):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', input_string)
txt = InsertSpacesAtCaps(txt)
txt = " ".join(txt)
print(txt)

#10_______________________________
print("10______________________")
def CamelCase_to_snake_case(camel_case):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case).lower()
txt1 = CamelCase_to_snake_case(txt1)
txt1 = " ".join(txt1)

text.close()
print(txt1)
