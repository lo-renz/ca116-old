#!/usr/bin/env python3

n = 10
smallest_positive = int(input())

i = 0
while i < n - 1:
   positive = int(input())
   if positive > 0 and positive <= smallest_positive:
      smallest_positive = positive
   i = i + 1

print(smallest_positive)
