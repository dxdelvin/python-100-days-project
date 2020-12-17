rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

rand = random.randint(1,3)
user_choice = input("type 1 for rock, type 2 for papers, type 3 for scissors\n")
user = int(user_choice)

print("User chooses")
if(user == 1):
  print(rock)
elif(user==2):
  print(paper)
else:
  if(user>3):
    print("Since you choose the number more than 3 so we defaulted your number to 3")
  print(scissors)
  

print("Computer Chooses")
if(rand == 1):
  print("ROCK")
  print(rock)
elif(rand==2):
  print("PAPER")
  print(paper)
elif(rand==3):
  print("SCISSORS")
  print(scissors)

if(rand == user):
  print("The Game Is Draw")
elif(user == 1 and rand==3):
  print("YOU WON THE GAME")
elif(user ==2 and rand==1):
  print("YOU WON THE GAME")
elif(user==3 and rand==2):
  print("YOU WON THE GAME")
else:
  print("YOU LOST THE GAME!!")