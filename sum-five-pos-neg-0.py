#!/usr/bin/env python3

total_neg = 0
total_pos = 0
n = int(input())

while n != 0:
   if n < 0:
      total_neg = total_neg + n
   else:
      total_pos = total_pos + n
   n = int(input())

print(total_neg, total_pos)
