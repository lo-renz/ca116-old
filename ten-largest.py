#!/usr/bin/env python3

n = 10
largest = int(input())

i = 0
while i < n - 1:
   v = int(input())
   if v > largest:
      largest = v
   i = i + 1

print(largest)
