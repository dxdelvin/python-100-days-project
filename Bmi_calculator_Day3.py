
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height**2)
round_bmi =round(bmi,1)
print(round_bmi)

if bmi<=18.5:
  print(f"Your bmi is {round_bmi} and you are underweight!!")
elif bmi<=25:
  print(f"Your bmi is {round_bmi} and you are Normal weight!!")
elif bmi<=30:
  print(f"Your bmi is {round_bmi} and you are overweight!!")
elif bmi<=35:
  print(f"Your bmi is {round_bmi} and you are Obese!!")
else:
  print(f"Your bmi is {round_bmi} and you are Clinacally Obese!!")
