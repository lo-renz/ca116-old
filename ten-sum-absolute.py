#!/usr/bin/env python3

n = 10
absolute_total = 0

i = 0
while i < n:
   absolute = int(input())
   if absolute < 0:
      absolute_total = (absolute * -1) + absolute_total
   else:
      absolute_total = absolute + absolute_total
   i = i + 1

print(absolute_total)
