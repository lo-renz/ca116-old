#!/usr/bin/env python3

weight = int(input())
height = int(input())

bmi = weight / (height * height) * 10000

if bmi < 18.5:
   print("underweight")
elif bmi >= 18.5 and bmi <= 24.9:
   print("normal")
elif bmi >= 25.0 and bmi <= 29.9:
   print("overweight")
elif bmi >= 30.0:
   print("obese")
else:
   print("normal")
