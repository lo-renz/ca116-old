#!/usr/bin/env python3

a = []
s = input()
while s != "end":
   i = 0
   while i < len(a) and s != a[i]:
      i = i + 1
   if i == len(a):
      a.append(s)
   s = input()

j = 0
while j < len(a):
   print(a[j])
   j = j + 1
