#!/usr/bin/env python
# -*- coding: utf-8 -*-
# line_count.py
import sys

count = 0
for line in sys.stdin:
    count += 1

# print schreibt nach sys.stdout
print count
