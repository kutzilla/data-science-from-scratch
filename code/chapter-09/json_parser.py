#!/usr/bin/env python
# -*- coding: utf-8 -*-
# json_parser.py
import json

serialized = """{ "title" : "Data Science Book",
    "author" : "Joel Grus",
    "publicationYear" : 2014,
    "topics" : ["data", "science", "data science"] }"""

# parse JSON und erhalte ein Python dict
deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
    print deserialized
