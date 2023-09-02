#!/usr/bin/env python3

import sys

s = sys.stdin.readline()
while s != "":
   i = 0
   while i < len(s) and s[i] != "(":
      i = i + 1

   j = i
   while j < len(s) and s[j] != ")":
      j = j + 1

   if j < len(s):
      inside = s[i + 1:j]

   if j < len(s):
      sys.stdout.write(inside + "\n")
   s = sys.stdin.readline()
