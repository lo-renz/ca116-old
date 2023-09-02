#!/usr/bin/env python3

a = []
s = input()
while s != "end":
   a.append(s)
   s = input()

i = int(input())
p = i
while i < len(a):
   if int(a[i]) < int(a[p]):
      p = i
   i = i + 1

print(p)
