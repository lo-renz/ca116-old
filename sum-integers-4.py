#!/usr/bin/env python3

import sys
file = sys.argv
total = 0

i = 1
while i < len(file):
   with open(file[i]) as f:
      numbers = f.readline()
      while numbers != "":
         t = numbers.split()
         j = 0
         while j < len(t):
            total = total + int(t[j])
            j = j + 1
         numbers = f.readline()
   i = i + 1

print(total)
