favBands = {"Twenty one pilots", "Imagine Dragons", "AJR", "Saint Motel", "OneRepublic", "5SOS"}
if "5SOS" in favBands:
    print ("I only listen to their new stuff")

favBands.add("X Ambassadors")
print (favBands)

kindalikeBands = {"Half Alive", "Fitz and The Tantrums", "Olivia Rodrigo", "The Weeknd"}
favBands.update(kindalikeBands)
print (favBands)

favBands.remove("The Weeknd")
print (favBands)

favBands.discard("Half Alive")
print (favBands)