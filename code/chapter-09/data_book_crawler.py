#!/usr/bin/env python
# -*- coding: utf-8 -*-
# data_book_crawler.py
from bs4 import BeautifulSoup
from collections import Counter
from time import sleep
import matplotlib.pyplot as plt
import requests
import re

def book_info(td):
    """Extrahiere aus einem Beautiful Soup-<td>-Tag für ein Buch die Details des
    Buches und gib ein dict zurück"""
    title = td.find("div", "thumbheader").a.text
    by_author = td.find('div', 'AuthorName').text
    authors = [x.strip() for x in re.sub("^By ", "", by_author).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).group()[0]
    date = td.find("span", "directorydate").text.strip()

    return {
        "title" : title,
        "authors" : authors,
        "isbn" : isbn,
        "date" : date
    }


def is_video(td):
    """Es ist ein Video, wenn es genau ein pricelabel gibt und wenn der Text
    im pricelabel nach strip() mit 'Video' beginnt"""
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and
            pricelabels[0].text.strip().startswith("Video"))

def get_year(book):
    """book["date"] enthält etwa 'November 2014', wir müsen am Leerzeichen
    teilen und den zweiten Teil nehmen"""
    return int(book["date"].split()[1])

base_url = "http://shop.oreilly.com/category/browse-subjects/data.do" + \
      "?sortby=publicationDate&page="

books = []

NUM_PAGES = 31 # während des Schreibens, inzwischen vermutlich mehr

for page_num in range(1, NUM_PAGES + 1):
    print "souping page", page_num, ",", len(books), " found so far"
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')

    for td in soup('td', 'thumbtext'):
        if not is_video(td):
            books.append(book_info(td))

year_counts = Counter(get_year(book) for book in books
                      if get_year(book) <= 2016)

years = sorted(year_counts)

book_counts = [year_counts[year] for year in years]
plt.plot(years, book_counts)
plt.ylabel("# of data books")
plt.title("Data is Big!")
plt.show()
