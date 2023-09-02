#!/usr/bin/env python3

total = 0
lines = input()
while lines != "end":
   tokens = lines.split()
   total = total + int(tokens[2])
   lines = input()

print(total)
