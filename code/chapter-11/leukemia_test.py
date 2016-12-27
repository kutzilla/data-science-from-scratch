#!/usr/bin/env python
# -*- coding: utf-8 -*-
# leukemia_test.py
from __future__ import division

def accuracy(tp, fp, fn, tn):
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total

def precision(tp, fp, fn, tn):
    return tp / (tp + fp)

def recall(tp, fp, fn, tn):
    return tp / (tp + fn)

# Harmonisches Mittel
def f1_score(tp, fp, fn, tn):
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)

    return 2 * p * r / (p + r)

print accuracy(70, 4930, 13930, 981070)

print precision(70, 4930, 13930, 981070)

print recall(70, 4930, 13930, 981070)

print f1_score(70, 4930, 13930, 981070)
