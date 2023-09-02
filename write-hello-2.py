#!/usr/bin/env python3

import sys
file_name = sys.argv[1]
message = "Hello world.\n"

with open(file_name, "w") as f:
   f.write(message)
