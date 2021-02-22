names = ["John" , "Jack"]

#Append adds an element to the back of a list
names.append("Ethan")
#Insert adds an element in the spocific position you want, moving the others to right of it
names.insert(0,"Jessica")
#Directly setting a index Location in the list removes what was there previously
names[1] = "nothing"
#Pop allows you to remove an item from a list
names.pop(1)

print (names)
second_name = "Jack"
#len is short for length and gets the amount of element to a list

amountofnames = len(names)

print(second_name)