#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
from matplotlib import pyplot as plt


grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()],  # verschiebe jeden Balken um 4
                                            # nach links
        histogram.values(),                 # gibt jedem Balken die korrekte Höhe
        8)                                  # gibt jedem Balken eine Breite von 8

plt.axis([-5, 105, 0, 5])                   # die x-Achse reicht von -5 bis 105,
                                            # die y-Achse reicht von 0 bis 5
plt.xticks([10 * i for i in range(11)])     # Beschriftung der x-Achse ist 0, 10,
                                            # ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()
