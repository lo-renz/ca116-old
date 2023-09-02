#!/usr/bin/env python3

n = int(input())
i = 0
x = 1
while i < n:
   if x % 3 == 0 and x % 5 == 0:
      print("fizz-buzz")
   elif x % 3 == 0:
      print("fizz")
   elif x % 5 == 0:
      print("buzz")
   else:
      print(x)
   i = i + 1
   x = x + 1
