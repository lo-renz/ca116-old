#!/usr/bin/env python3

f = input()

j = 0
while f[j] != ".":
   j = j + 1
print(f[:j])

i = 0
while f[i] != ".":
   i = i + 1
print(f[i + 1:])
