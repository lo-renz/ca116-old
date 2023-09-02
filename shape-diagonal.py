#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
   if i != 0:
      print((" " * i) + "*")
   else:
      print("*")
   i = i + 1
