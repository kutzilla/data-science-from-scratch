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
