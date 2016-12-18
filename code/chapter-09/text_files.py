#!/usr/bin/env python
# -*- coding: utf-8 -*-
# text_files.py
import re

# 'r' bedeutet nur lesen
file_for_reading = open('reading_file.txt', 'r')

# 'w' zum Schreiben -- überschreibt eine bereits existierende Datei!
file_for_writing = open('writing_file.txt', 'w')

# 'a' zum Anhängen -- am Ende einer Datei
file_for_appending = open('appending_file.txt', 'a')

# vergessen Sie nicht, Ihre Datei wieder zu schließen
file_for_reading.close()


starts_with_hash = 0

with open('reading_file.txt', 'r') as file:
    for line in file:
        if re.match('^#', line):
            starts_with_hash += 1

print starts_with_hash
