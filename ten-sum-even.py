#!/usr/bin/env python3

n = 10
even_total = 0

i = 0
while i < n:
   m = int(input())
   if m % 2 == 0:
      even_total = m + even_total
   i = i + 1

print(even_total)
