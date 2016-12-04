#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

variance        = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared    = [256, 128, 64, 32, 16, 8, 4, 2 ,1]
total_error     = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# wir können plt.plot mehrmals aufrufen,
# um mehrere Datenreihen in einem Diagramm darzustellen
plt.plot(xs, variance, 'g-', label= 'variance')         # grüne durchgängige Linie
plt.plot(xs, bias_squared, 'r-.', label= 'bias^2')      # rote gestrichelte Linie
plt.plot(xs, total_error, 'b:', label= 'total error' )  # blaue gepunktete Linie

# weil wir jeder Datenreihe ein Label zugewiesen haben,
# bekommen wir die Legende frei Haus
# loc=9 bedeutet "oben mittig"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()
