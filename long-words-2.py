#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["cat", "elephant", "mouse", "lizard", "horse", "mongoose"]

b = []

i = 0
while i < len(a):
   if len(a[i]) >= 6:
      b.append(a[i])
      i = len(a)
   i = i + 1

print(b[0])
