#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Ghandi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# Balken haben standardmäßig die Breite 0.8, daher fügen wir
# zur linken Koordinate 0.1 hinzu, sodass die Balken zentriert sind
xs = [i + 0.1 for i, _ in enumerate(movies)]

# plotte die Balken mit den Koordinaten der linken Seite [xs] und der Höhe
[num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# beschrifte die x-Achse mit den Namen der Filme in der Mitte der Balken
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()
