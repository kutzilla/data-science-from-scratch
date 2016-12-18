#!/usr/bin/env python
# -*- coding: utf-8 -*-
# html_parser.py
from bs4 import BeautifulSoup
import requests

html = requests.get('http://www.example.com').text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p') # soup.p ist äquivalent

first_paragraph_text = soup.p.text

first_paragraph_words = soup.p.text.split()

first_paragraph_id = soup.p.get('id')

important_paragraphs = soup('p', {'class' : 'important'})

important_paragraphs2 = soup('p', 'important')

important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])]

spans_inside_divs = [span
                     for div in soup('div')
                     for span in div('span')]
