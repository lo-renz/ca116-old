#!/usr/bin/env python3

import sys

file_name = sys.stdin.readline()
while file_name != "":
   a = file_name.split("/")
   a = a[len(a) - 1].split("\n")
   print(a[0])
   file_name = sys.stdin.readline()
