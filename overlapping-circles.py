#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())

x2 = int(input())
y2 = int(input())
r2 = int(input())

dx = x2 - x1
dy = y2 - y1

h = (dx * dx) + (dy * dy)

if h < ((r1 + r2) ** 2):
   print("yes")
else:
   print("no")
