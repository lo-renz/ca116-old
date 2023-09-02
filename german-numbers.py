#!/usr/bin/env python3

import sys

english = "one two three four five six seven eight nine ten"
german = "eins zwei drei vier funf sechs sieben acht neun zehn"

translation = {}
english = english.split()
german = german.split()

i = 0
i = 0
while i < len(english):
   translation[english[i]] = german[i]
   i = i + 1

word = sys.stdin.readline().strip()
while 0 < len(word):
   if word in translation:
      print(translation[word])
   word = sys.stdin.readline().strip()
