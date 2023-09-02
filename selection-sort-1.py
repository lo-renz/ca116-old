#!/usr/bin/env python3

a = []
s = input()
while s != "end":
   a.append(s)
   s = input()

p = 0
i = 1
while i < len(a):
   if int(a[i]) < int(a[p]):
      p = i
   i = i + 1

print(p)
