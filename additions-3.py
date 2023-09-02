#!/usr/bin/env python3

a = 0
b = 0

i = 0
while int(a) + int(b) != 1000:
   s = input()
   j = 0
   while j < len(s) and (s[j] != "+"):
      j = j + 1
   a = s[:j]
   b = s[j + 1:]
   print(int(a) + int(b))
   i = i + 1
