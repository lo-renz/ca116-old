#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
   j = n // 2 - i
   if j < 0:
      j = -j

   if j == 0:
      print(n // 2 * " " + "*")
   else:
      print((n // 2 - j) * " " + "*" + (2 * j - 1) * " " + "*")
   i = i + 1
