#!/usr/bin/env python3

import sys

translations = {
   "one": "eins",
   "two": "zwei",
   "three": "drei",
   "four": "vier",
   "five": "funf",
   "six": "sechs",
   "seven": "sieben",
   "eight": "acht",
   "nine": "neun",
   "ten": "zehn",
}

number = sys.stdin.readline().strip()
while 0 < len(number):
   if number in translations:
      print(translations[number])
   number = sys.stdin.readline().strip()
