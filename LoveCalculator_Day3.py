
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name_lower1 = name1.lower()
name_lower2 = name2.lower()

t1 = name_lower1.count('t')
r1 = name_lower1.count('r')
u1 = name_lower1.count('u')
e1 = name_lower1.count('e')

l1 = name_lower1.count('l')
o1 = name_lower1.count('o')
v1 = name_lower1.count('v')
e3 = name_lower1.count('e')

t2 = name_lower2.count('t')
r2 = name_lower2.count('r')
u2 = name_lower2.count('u')
e2 = name_lower2.count('e')

l2 = name_lower2.count('l')
o2 = name_lower2.count('o')
v2 = name_lower2.count('v')
e4 = name_lower2.count('e')

true_ = t1+t2+r1+r2+u1+u2+e1+e3
love_ = l1+l2+o1+o2+v1+v2+e1+e4

lovescore_str = str(true_)+str(love_)
lovescore = int(lovescore_str)


if lovescore < 10 or lovescore > 90:
    print(f"Your lovescore is {lovescore}% and you are both like coke and mentos")
elif lovescore < 50 and lovescore > 40:
    print(f"your lovescore is {lovescore}% and you both are alright together!!")
else:
    print("your lovescore is " + str(lovescore) + "%")