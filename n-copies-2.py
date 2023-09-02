#!/usr/bin/env python3

s = input()
n = int(input())

copies = ((s * (0 < n)) + ("-" + s) * (n - 1))

print(copies)
