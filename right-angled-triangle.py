#!/usr/bin/env python3

s1 = int(input())
s2 = int(input())
s3 = int(input())

hypotenuse = s1 * s1
other_side_1 = s2 * s2
other_side_2 = s3 * s3

right_angled_triangle = hypotenuse == other_side_1 + other_side_2

# right_angled_triangle = s1 > (s2 and s3)

print(right_angled_triangle)

# s1 ** 2 = (s2 ** 2) + (s3 ** 2)
