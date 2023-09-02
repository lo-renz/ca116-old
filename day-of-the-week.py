#!/usr/bin/env python3

month = int(input())
dom = int(input())

dow = ((month - 1) * 30) + dom - 1
print((dow % 7) + 1)
