#!/usr/bin/env python
# -*- coding: utf-8 -*-
# linear_regression.py
from statistics import correlation, standard_deviation, mean, de_mean
from matplotlib import pyplot as plt
from vectors import vector_subtract, scalar_multiply
import random

def predict(alpha, beta, x_i):
    return beta * x_i + alpha

def error(alpha, beta, x_i, y_i):
    """Fehler der Vorhersage beta * x_i + alpha
    mit dem tatsächlichen Wert für y_i"""
    return y_i - predict(alpha, beta, x_i)

def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2 for x_i, y_i in zip(x, y))

def least_squared_fit(x, y):
    """findet mit Trainingsdaten für x und y
    die Kleinste-Quadrate-Werte für alpha und beta"""
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta

def total_sum_of_squares(y):
    """gesamte quadratische Abweichung der y_i vom Mittelwert"""
    return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha, beta, x, y):
    """Anteile der vom Modell abgedeckten Streuung von y, entspricht
    1 - Anteil der nicht vom Modell abgedeckten Streuung von y"""

    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) /
                  total_sum_of_squares(y))

def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2

def squared_error_gradient(x_i, y_i, theta):
    alpha, beta = theta
    return [-2 * error(alpha, beta, x_i, y_i),          # partielle Ableitung alpha
            -2 * error(alpha, beta, x_i, y_i) * x_i]    # partielle Ableitung beta

def in_random_order(data):
    """generator that returns the elements of data in random order"""
    indexes = [i for i, _ in enumerate(data)]  # create a list of indexes
    random.shuffle(indexes)                    # shuffle them
    for i in indexes:                          # return the data in that order
        yield data[i]


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):

    data = zip(x, y)
    theta = theta_0                             # initial guess
    alpha = alpha_0                             # initial step size
    min_theta, min_value = None, float("inf")   # the minimum so far
    iterations_with_no_improvement = 0

    # if we ever go 100 iterations with no improvement, stop
    while iterations_with_no_improvement < 100:
        value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )

        if value < min_value:
            # if we've found a new minimum, remember it
            # and go back to the original step size
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            # otherwise we're not improving, so try shrinking the step size
            iterations_with_no_improvement += 1
            alpha *= 0.9

        # and take a gradient step for each of the data points
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta


num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,
               13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,
               9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,
               7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
               5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
               4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,
               2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,
                 54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,
                 35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,
                 21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,
                 40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,
                 40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,
                 28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,
                 44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,
                 31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,
                 34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,
                 40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,
                 27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,
                 14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,
                 32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,
                 18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,
                 32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,
                 35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,
                 30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,
                 24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,
                 23.48,8.38,27.81,32.35,23.84]

outlier = num_friends.index(100) # Index des Ausreißers

num_friends_good = [x for i, x in enumerate(num_friends) if i != outlier]

daily_minutes_good = [x for i, x in enumerate(daily_minutes) if i != outlier]

alpha, beta = least_squared_fit(num_friends_good, daily_minutes_good)

print "Alpha:\t\t", alpha
print "Beta:\t\t", beta
print "R-Quadrat:\t", r_squared(alpha, beta, num_friends_good, daily_minutes_good)

x = [i for i in range(100)]
y = [predict(alpha, beta, i) for i in x]

plt.plot(x, y, color="black")
plt.title("Simple Linear Regression Model")
plt.xlabel("# of friends")
plt.ylabel("# of minutes")

for x_i, y_i in zip(num_friends_good, daily_minutes_good):
    plt.scatter(x_i, y_i, color="lightgray")

plt.show()

# wähle eine Zufallswert zum Starten
random.seed(0)

theta = [random.random(), random.random()]
alpha, beta = minimize_stochastic(squared_error,
                                  squared_error_gradient,
                                  num_friends_good,
                                  daily_minutes_good,
                                  theta,
                                  0.0001)

print "New Alpha:\t", alpha
print "New Beta:\t", beta
