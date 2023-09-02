#!/usr/bin/env python3

mark = int(input())

first = mark >= 70
second = mark >= 50 and mark < 70
third = mark >= 40 and mark < 50
fail = mark < 40

print("first:", first)
print("second:", second)
print("third:", third)
print("fail:", fail)
