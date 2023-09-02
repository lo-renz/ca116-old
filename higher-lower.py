#!/usr/bin/env python3

curr = int(input())
prev = 0

i = 0
while i < 5:
   prev = int(input())
   if curr < prev:
      print("higher")
   elif curr > prev:
      print("lower")
   else:
      print("equal")
   curr = prev
   i = i + 1
