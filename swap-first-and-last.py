#!/usr/bin/env python3

s = input()

first = s[0]
last = s[len(s) - 1]
middle = s[1:len(s) - 1]

print(last + middle + first)
