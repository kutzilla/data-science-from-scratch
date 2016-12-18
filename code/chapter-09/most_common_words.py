#!/usr/bin/env python
# -*- coding: utf-8 -*-
# most_common_words.py
import sys
from collections import Counter

# Anzahl Wörter als erstes Argument
try:
    num_words = int(sys.argv[1])
except:
    print "usage: most_common_words.py num_words"
    sys.exit(1) # ein exit code ungleich null bedeutet 'Fehler'

counter = Counter(word.lower()                      # Kleinbuchstaben
                  for line in sys.stdin              #
                  for word in line.strip().split()  # teile bei Leerzeichen
                  if word)                          # überspringe leere 'Wörter'

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
