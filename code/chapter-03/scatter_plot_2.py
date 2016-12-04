#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")

# Sorgt dafür, dass die Achsen gleich sind
# und somit kein irreführendes Bild entsteht
plt.axis("equal")

plt.show()
