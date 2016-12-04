#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)

plt.ylabel("# of times I heard someone say 'data science'")

# ohne diesen Befehl beschriftet matplotlib die x-Achse mit 0, 1
# und fügt +2.013e3 ganz in der Ecke hinzu (böses matplotlib!)
plt.ticklabel_format(useOffset=False)

# die irreführende y-Achse zeigt nur den Teil über 500
plt.axis([2012.5, 2014.5, 0, 550])
plt.title("Not So Huge Anymore")
plt.show()
