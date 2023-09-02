#!/usr/bin/env python3

n = 10
smallest_even = int(input())

i = 0
while i < n - 1:
   even = int(input())
   if even % 2 == 0 and even < smallest_even:
      smallest_even = even
   i = i + 1

print(smallest_even)
