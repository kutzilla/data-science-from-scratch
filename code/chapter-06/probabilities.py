#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from collections import Counter
from matplotlib import pyplot as plt
import random
import math

def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print "P(both | older):", both_girls / older_girl
print "P(both | either):", both_girls / either_girl

def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    if x < 0: return 0 # der gleichverteilte Zufallswert ist nie kleiner 0
    elif x < 1: return x # z.B. P(X <= 0.4) = 0.4
    else: return 1 # der gleichverteilte Zufallswert ist immer kleiner 1

def normal_pdf(x, mu = 0, sigma = 1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu = 0, sigma = 1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):

    data = [binomial(n, p) for _ in range(num_points)]

    # zeige die Stichprobe der Binomialverteilung als Balken
    histogram = Counter(data)

    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
             0.8,
             color = '0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # zeige genährte Normalverteilung als Linie
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distrbution vs Normal Approximation")
    plt.show()

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label = 'mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label = 'mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label = 'mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-', label = 'mu=-1,sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label = 'mu=0,sigma=1')
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '-', label = 'mu=0,sigma=2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], '-', label = 'mu=0,sigma=0.5')
plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-', label = 'mu=-1,sigma=1')
plt.legend(loc=4) # bottom right
plt.title("Various Normal cdfs")
plt.show()

make_hist(0.75, 100, 10000)
