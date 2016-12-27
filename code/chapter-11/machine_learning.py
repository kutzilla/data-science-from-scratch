#!/usr/bin/env python
# -*- coding: utf-8 -*-
# machine_learning.py
import random

def split_data(data, prob):
    """teile die Daten in Fraktionen [prob, 1 - prob]"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def train_test_split(x, y, test_pct):
    data = zip(x, y)                                # Paare korresporendierender Werte
    train, test = split_data(data, 1 - test_pct)    # teile die Datenpaare
    x_train, y_train = zip(*train)                  # magisches Entzippen
    x_test, y_test = zip(*test)
    retrun x_train, x_test, y_train, y_test
