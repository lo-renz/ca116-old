#!/usr/bin/env python3

n = 10
total_positive = 0

i = 0
while i < n:
   positive = int(input())
   if positive > 0:
      total_positive = positive + total_positive
   i = i + 1

print(total_positive)
