#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from matplotlib import pyplot as plt
from collections import Counter
import math

def mean(x):
    return sum(x) / len(x)

def median(v):
    """"finde den Wert aus v, der 'in der Mitte' liegt"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # bei ungerader Anzahl liefere den Wert aus der Mitte
        return sorted_v[midpoint]
    else:
        # bei gerader Anzahl liefere den Durchschnitt der beiden mittleren Werte
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[hi] + sorted_v[lo]) / 2

def quantile(x, p):
    """liefert den Wert für das p-te Perzentil in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    """liefert eine Liste, es kann mehr als einen Modus geben"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count == max_count]

# "range" für die Streuung ist in Python bereits belegt, daher der andere Name
def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    """verschiebe x durch Abziehen des Mittelwerts (das Ergebnis hat den
    Mittelwert 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

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

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

def covariance(x, y):
    """"Große positive Kovarianz bedeutet, dass x tendenziell groß ist,
    wenn auch y groß ist, und klein, wenn y klein ist. Große negative Kovarianz
    bedeutet das Gegenteil. Kovarianz nahe null bedeutet, dass kein solcher
    Zusammenhang besteht"""
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    """Gibt einen Wert zwischen -1 (perfekte negative Korrelation) und
    1 (perfekte Korrelation) zurück"""
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # wenn es keine Streuung gibt, ist die Korrelation gleich 0

def make_num_friends_histogram(num_friends):
    friend_counts = Counter(num_friends)
    xs = range(101)
    ys = [friend_counts[x] for x in xs]
    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25])
    plt.title("Histogram of Friend Counts")
    plt.xlabel("# of friends")
    plt.ylabel("# of people")
    plt.show()

def make_daily_minutes_histogram(daily_minutes):
    daily_minutes_clean = [int(i) for i in daily_minutes]
    dm_counts = Counter(daily_minutes_clean)
    xs = range(101)
    ys = [dm_counts[x] for x in xs]
    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25])
    plt.title("Histogram of Friend Counts")
    plt.xlabel("# of daily minutes")
    plt.ylabel("# of people")
    plt.show()

def make_friends_daily_minutes_correlation(x, y):
    for friend_count, minute_count in zip(x, y):
        plt.scatter(x, y)

    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.show()
