#!/usr/bin/env python3

timetable = []
lines = input()
while lines != "end":
   timetable.append(lines)
   lines = input()

n = input()

i = 0
while i < len(timetable):
   if int(timetable[i][0]) == int(n):
      print(timetable[i])
   i = i + 1
