#!/usr/bin/env python3

import sys

punctuation = {
   ".": "1",
   ",": "1",
   "!": "1",
   "?": "1",
   ";": "1",
   ":": "1",
}

total = 0
sum = sys.stdin.readlines()
while 0 < len(sum):
   if sum in punctuation:
      total = int(punctuation[sum]) + 1
   sum = sys.stdin.readlines()

print(total)
