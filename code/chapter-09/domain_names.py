#!/usr/bin/env python
# -*- coding: utf-8 -*-
# domain_names.py
from collections import Counter

def get_domain(email_address):
    """trenne am @ und gib den letzten Teil zurück"""
    return email_address.lower().split("@")[-1]

with open('email_address.txt', 'r') as file:
    domain_counts = Counter(get_domain(line.strip())
                            for line in file
                            if "@" in line)

print domain_counts
