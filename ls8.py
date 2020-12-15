#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

if len(sys.argv) == 2:
  cpu.load(sys.argv[1])
  cpu.run()
else:
  print(f'file name is missing. ex. "python3 ls8.py <filename>"')