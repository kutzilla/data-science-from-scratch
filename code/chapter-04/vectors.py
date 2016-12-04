#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from functools import partial
import math

def vector_add(v, w):
    """addiert die korrespondierenden Elemente"""
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """subtrahiert die korrespondierenden Elemente"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum1(vectors):
    """summiert alle korrespondierenden Elemente auf """
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def vector_sum2(vectors):
    return reduce(vector_add, vectors)

vector_sum3 = partial(reduce, vector_add)

def scalar_multiply(c, v):
    """c ist eine Zahl, v ist ein Vektor"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """berechne den Vektor, dessen i-tes Element der Mittelwert der i-ten Elemente der Eingabevektoren ist"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum3(vectors))

def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def distance(v, w):
    return magnitude(vector_subtract(v, w))

height_weight_age = [70,     # Zoll
                     170,   # Pfund
                     40 ]   # Jahre

grades = [95,   # exam1
          80,   # exam2
          75,   # exam3
          62 ]  # exam4


vec1 = [6, 9, 8]
vec2 = [3, 5, 2]
vec3 = [9, 4, 8]

print "Addition:\t", vector_add(vec1, vec2)
print "Subtraktion:\t", vector_subtract(vec1, vec2)
print "Summe 1:\t", vector_sum1([vec1, vec2, vec3])
print "Summe 2:\t", vector_sum2([vec1, vec2, vec3])
print "Summe 3:\t", vector_sum3([vec1, vec2, vec3])
print "Skalar:\t\t", scalar_multiply(2, vec1)
print "Mittelwert:\t", vector_mean([vec1, vec2, vec3])
print "Skalarprodukt:\t", dot(vec1, vec2)
print "Quadratsumme:\t", sum_of_squares(vec1)
print "Vektorlänge:\t", magnitude(vec1)
print "Vektordistanz:\t", distance(vec1, vec2)
