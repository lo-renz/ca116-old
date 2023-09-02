#!/usr/bin/env python3

numbers = []
s = input()
while s != "end":
   numbers.append(s)
   s = input()

odd = []
i = 0
while i < len(numbers):
   if int(numbers[i]) % 2 == 0:
      print(numbers[i])
   else:
      odd.append(numbers[i])
   i = i + 1

j = 0
while j < len(odd):
   print(odd[j])
   j = j + 1
