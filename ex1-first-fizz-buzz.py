#!/usr/bin/env python3

i = 0
while i < 7:
   n = int(input())
   if (n % 5 == 0 and n % 3 == 0) != 1:
      print(n)
   i = i + 1
