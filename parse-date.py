#!/usr/bin/env python3

s = input()

#stdout == October 23rd, 2018 (Tuesday)

#day
i = 0
while s[i] != " ":
   i = i + 1
day = s[:i]

#no.
j = i + 1
while s[j] != " ":
   j = j + 1
no = s[i + 1:j]

#month
i = j + 1
while s[i] != " ":
   i = i + 1
month = s[j + 1:i - 1]

#year
j = i + 1
while j < len(s):
   j = j + 1
year = s[i + 1:j]

print(month + " " + no + "," + " " + year + " " + "(" + day + ")")
