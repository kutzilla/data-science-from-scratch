#!/usr/bin/env python
# -*- coding: utf-8 -*-
# egrep.py
import sys, re

# sys.argv ist die Liste Kommandozeilenparameter
# sys.argv[0] ist der Name des Programms selbst
# sys.argv[1] ist der eingegebene reguläre Ausdruck
regex = sys.argv[1]

# für jede ins Skript gefütterte Zeile
for line in sys.stdin:
    # wenn der Ausdruck zutrifft, schreibe nach stdout
    if re.search(regex, line):
        sys.stdout.write(line)
