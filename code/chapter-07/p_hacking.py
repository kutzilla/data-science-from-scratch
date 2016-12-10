#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from collections import Counter
from matplotlib import pyplot as plt
import random
import math

def run_experiment():
    """wirf eine ausgewogene Münze 1000 Mal, True = Kopf, False = Zahl"""
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):
    """verwende ein Signifikanzniveau von 5%"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531

random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment
                      for experiment in experiments
                      if reject_fairness(experiment)])

print num_rejections
