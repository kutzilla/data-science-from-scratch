#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from functools import partial
from collections import Counter
from matplotlib import pyplot as plt
import random
import math

def vector_subtract(v, w):
    """subtrahiert die korrespondierenden Elemente"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def distance(v, w):
    return magnitude(vector_subtract(v, w))

def sum_of_squares(v):
    """berechnet die Summe der quadrierten Elemente von v"""
    return sum(v_i ** 2 for v_i in v)

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def square(x):
    return x * x

def derivative(x):
    return 2 * x

derivative_estimate = partial(difference_quotient, square, h = 0.00001)

# zeige im Plot, dass beide in etwa gleich sind
x = range(-10, 10)
plt.title("Actual Derivates vs. Estimates")
plt.plot(x, map(derivative, x), 'rx', label='Actual')            # rotes x
plt.plot(x, map(derivative_estimate, x), 'b+', label='Estimate') # blaues +
plt.legend(loc=9)
plt.show()


def partial_difference_quotient(f, v, i, h):
    """berechne die i-te partielle Ableitung von f nach v"""
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)] # füge h nur zum i-ten Element hinzu
    return (f(w) - f(v)) - h

def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]



def step(v, direction, step_size):
    """gehe step_size in Richtung v"""
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

# wähle einen zufälligen Ausgangspunkt
v = [random.randint(-10, 10) for i in range(3)]

tolerance = 0.0000001

while True:
    gradient = sum_of_squares_gradient(v)   # berechne den Gradient bei v
    next_v = step(v, gradient, -0.01)       # gehe einen Schritt am Gradienten
                                            # rückwärts
    if distance(next_v, v) < tolerance:
            break
    v = next_v
    print v
