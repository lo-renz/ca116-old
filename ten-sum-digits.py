#!/usr/bin/env python3

n = 10
total = 0

i = 0
while i < n:
   digits = int(input())
   if digits >= 0:
      least_significant_digit = digits % 10
   elif digits < 0:
      least_significant_digit = (digits * -1) % 10
   total = total + least_significant_digit
   i = i + 1

print(total)
