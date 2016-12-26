#!/usr/bin/env python
# -*- coding: utf-8 -*-
# rescaling.py
import math

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v, v)

def variance(x):
    """setzt vorraus, dass x mindestens 2 Elemente enthält"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def mean(x):
    return sum(x) / len(x)

def de_mean(x):
    """verschiebe x durch Abziehen des Mittelwerts (das Ergebnis hat den
    Mittelwert 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def scale(data_matrix):
    """liefert Mittelwert und Standardabweichung für jede Spalte"""
    num_rows, num_cols = shape(data_matrix)

    means = [mean(get_column(data_matrix, j))
             for j in range(num_cols)]

    stdevs = [standard_deviation(get_column(data_matrix, j))
              for j in range(num_cols)]

    return means, stdevs

def rescale(data_matrix):
    """skaliert die Eingabedaten um, sodass jede Spalte
    den Mittelwert 0 und die Standardabweichung 1 hat
    Spalten ohne Streuung werden nicht angetastet"""
    means, stdevs = scale(data_matrix)

    def rescaled(i, j):
        if stdevs[j] > 0:
            return (data_matrix[i][j] - means[j]) / stdevs[j]
        else:
            return data_matrix[i][j]

    num_rows, num_cols = shape(data_matrix)
    return make_matrix(num_rows, num_cols, rescaled)


persons = [ [63, 67, 70],
            [160, 170.2, 177.8],
            [150, 160, 171]]

print persons
print rescale(persons)
