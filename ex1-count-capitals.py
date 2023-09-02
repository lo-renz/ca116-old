#!/usr/bin/env python3

s = input()
total = 0

# ("A" <= s[i] and s[i] <= "Z")

i = 0
while i < len(s):
   if ("A" <= s[i] and s[i] <= "Z"):
      caps = s[i]
      length = len(caps)
      total = total + len(caps)
   i = i + 1

print(total)
