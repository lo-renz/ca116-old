#!/usr/bin/env python3

import sys
args = sys.argv[1:]

a = []
i = 0
while i < len(args):
   a.append(int(args[i]))
   i = i + 1

total = 0
j = 0
while j < len(a):
   total = total + a[j]
   j = j + 1

print(total)
