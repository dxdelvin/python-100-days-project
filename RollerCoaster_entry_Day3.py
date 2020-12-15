print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("Welcome you can ride the rolecoaster\n")
    age = int(input("What is your age?"))
    if age > 18:
        bill = 12
        print("Your ticket price is $12")
    elif age < 12:
        bill = 5
        print("Your ticket price is $5")
    else:
        bill = 7
        print("Your ticket price is $7")

    if age < 55 and age > 45:
        print("your ticket is free!!")
        bill = 0
else:
    msg = "you cant ride into the roller coaster"
    print(msg)

photo = "do you want to click a photo you need to pay 3 dollars write 'yes' or 'no'"
if input(photo) == "yes":
    bill += 3

print(f"You need to pay ${bill}")