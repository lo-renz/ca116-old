#!/usr/bin/env python3

l1 = str(input())
l2 = str(input())
l3 = str(input())

l1_length = len(l1)
l2_length = len(l2)
l3_length = len(l3)

if l1_length > l2_length and l1_length > l3_length:
   print(l1)
elif l2_length > l1_length and l2_length > l3_length:
   print(l2)
elif l3_length > l1_length and l3_length > l2_length:
   print(l3)
