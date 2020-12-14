print("Welcome to Tip and Spilt your Bill Calculator!\n")
bill = input("What was your Total Bill???\n")
bill_as_int = int(bill)
print("What amount of tip you want to provide")
tip = input("5%,10%,15%,20%\n")
tip_as_int = int(tip)
Final_bill = bill_as_int + ((tip_as_int/100)*bill_as_int)
people = input("How many people want to split their bill\n")

round(Final_bill)
people_as_int = int(people)
split_bill = Final_bill/people_as_int
round(split_bill)

message = f"\nyour final bill is {Final_bill} and each of you can pay {split_bill}"
print(message)