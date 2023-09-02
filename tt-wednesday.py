#!/usr/bin/env python3

lines = input()
while lines != "end":
   tokens = lines.split()
   if tokens[0] == "3":
      print(" ".join(tokens[:]))
   lines = input()
