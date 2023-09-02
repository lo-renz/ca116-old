#!/usr/bin/env python3

n = int(input())

previous = 0
current = 1
fib_n = 0

a = []

i = 0
while fib_n < n:
   previous = current
   current = fib_n
   fib_n = previous + current
   a.append(fib_n)
   i = i + 1

j = 0
while j < len(a) and a[j] != n:
   j = j + 1

if a[j] == n:
   print("yes")
else:
   print("no")
