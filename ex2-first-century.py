#!/usr/bin/env python3

n = 5
gore = []

i = 0
while i < n:
   number = int(input())
   if number >= 100:
      gore.append(number)
   i = i + 1

if len(gore) != 0:
   print(gore[0])
else:
   print("none")
