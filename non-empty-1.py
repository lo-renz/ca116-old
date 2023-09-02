#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

b = []

i = 0
while i < len(a):
  if a[i] != "":
    b.append(a[i])
  i = i + 1

print(len(b))
