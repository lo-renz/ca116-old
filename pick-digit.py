#!/usr/bin/env python3

n = int(input())
p = int(input())

if p == 0:
   print(n % 10)
elif p == 1:
   print((n % 100) // 10)
elif p == 2:
   print((n % 1000) // 100)
elif p == 3:
   print((n % 10000) // 1000)
elif p == 4:
   print((n % 100000) // 10000)
else:
   print((n % 1000000) // 100000)
