#!/usr/bin/env python3

s = input()
total = 0

i = 0
while i < len(s):
   bin = int(s[i])
   dec = bin * (2 ** int(len(s) - i - 1))
   total = total + dec
   i = i + 1

print(total)
