import random
names_string = input ("Enter everyone names and use ',' after each name ")
names = names_string.split (", ")
lenth_names = len (names)
rand = random.randint (0, lenth_names)
print (f" the person going to pay is {names[rand]-1}")
