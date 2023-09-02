#!/usr/bin/env python3

n = int(input())

n1 = n // 100
m2d = n1 % 100

d1 = m2d // 10
d2 = m2d % 10

fr = (d2 * 10) + d1
print(fr)
