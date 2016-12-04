#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# erstelle ein Liniendiagramm, Jahre auf der x-Achse, GDP auf der y-Achse
plt.plot(years, gdp, color= 'green', marker= 'o', linestyle= 'solid')

# füge einen Titel hinzu
plt.title("Nominal GDP")

# beschrifte die y-Achse
plt.ylabel("Billions of $")
plt.show()
