#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from collections import Counter
from matplotlib import pyplot as plt
import random
import math

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0            # normal_cdf(-10) is (very close to) 0
    hi_z,  hi_p  =  10.0, 1            # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2     # consider the midpoint
        mid_p = normal_cdf(mid_z)      # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z

def normal_approximation_to_binomial(n, p):
    """findet das der Binomialverteilung(n, p) entsprechende My und Sigma"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

def normal_cdf(x, mu = 0, sigma = 1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# die normalverteilte kVf ist die Wahrscheinlichkeit, dass die Variable unter
# einer Schwelle liegt
normal_probability_below = normal_cdf

# wenn sie nicht unter der Schwelle liegt, liegt sie darüber
def normal_probability_above(lo, mu = 0, sigma = 1):
    return 1 - normal_cdf(lo, mu, sigma)

# liegt sie unter hi und nicht unter lo, liegt sie dazwischen
def normal_probability_between(lo, hi, mu = 0, sigma = 1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# sie liegt außerhalb, wenn sie nicht dazwischen liegt
def normal_probability_outside(lo, hi, mu = 0, sigma = 1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu = 0, sigma = 1):
    """berechnet sas z, bei de, P(Z <= z) = probability ist"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu = 0, sigma = 1):
    """berechnet das z, bei dem P(Z >= z) = probability ist"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu = 0, sigma = 1):
    """berechnet die symmetrischen Grenzen (um den Mittelwert), die die
       angegebene Wahrscheinlichkeit enthalten"""
    tail_probability = (1 - probability) / 2

    # tail_probability sollte oberhalb der oberen Grenze liegen
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # tail_probability sollte unterhalb er unteren Grenze liegen
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

print mu_0
print sigma_0


# 95-%-Grenze basierend auf der Annahme p = 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# Werte für mu und sigma basierend auf p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# bei einem Fehler 2. Art verwerfen wir die Nullhypothese irrtürmlich nicht
# was passiert, falls X noch immer im ursprünglichen Intervall liegt
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)

power = 1 - type_2_probability
print power

hi = normal_upper_bound(0.95, mu_0, sigma_0)

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability
print power

def two_sided_p_value(x, mu = 0, sigma = 1):
    if x >= mu:
        # liegt x über dem Mittelwert, ist das Intervall alles oberhalb von x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # liegt x unter dem Mittelwert, ist das Intervall alles unterhalb von x
        return 2 * normal_probability_below(x, mu, sigma)

print two_sided_p_value(529.5, mu_0, sigma_0)

#extreme_value_count = 0
#for _ in range(100000):
#    num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))
#    if num_heads >= 530 or num_heads <= 470:
#        extreme_value_count += 1

#print extreme_value_count / 100000


p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)

print normal_two_sided_bounds(0.95, mu, sigma)
