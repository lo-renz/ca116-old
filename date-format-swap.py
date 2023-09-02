#!/usr/bin/env python3

mmddyy = int(input())

yy = mmddyy % 100

# usdate
mm = mmddyy // 10000
dd1 = mmddyy % 10000
dd2 = dd1 // 100

# eudate
dd2 = dd2 * 10000
mm = mm * 100

ddmmyy = dd2 + mm + yy

print(ddmmyy)
