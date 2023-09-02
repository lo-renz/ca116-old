#!/usr/bin/env python3

file_name = "hello.txt"
message = "Hello world.\n"

with open(file_name, "w") as f:
   f.write(message)
