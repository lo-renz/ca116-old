#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and (s[i] < "0" or "9" < s[i]):
   i = i + 1

j = i
while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
   j = j + 1

k = j
while k < len(s) and (s[k] < "0" or "9" < s[k]):
   k = k + 1

if i < len(s):
   i = k
   while i < len(s) and ("0" <= s[i] and s[i] <= "9"):
      i = i + 1
   print(s[k:i], k)
