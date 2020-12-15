
print("Welcome to DX Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

print("\nYour Dx Pizza Bill\n")
bill = 0

if size == "S":
  bill = 15
  print("Small Pizza: $15")
elif size =="M":
  bill = 20
  print("Medium Pizza: $20")
elif size == "L":
  bill=25
  print("Large Pizza: $25")

if add_pepperoni == "Y" and size =="S":
  print("Pepperoni for Small Pizza: +$2")
  bill += 2
elif add_pepperoni == "Y" and (size =="L" or size =="M"):
  print("Pepperoni for Medium or Large Pizza: +$3")
  bill+=3

if extra_cheese == "Y":
  print("Extra cheese for any size pizza: + $1")
  bill += 1

print(f"\n Your Total Bill Amounts to ${bill}")
