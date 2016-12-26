#!/usr/bin/env python
# -*- coding: utf-8 -*-
# adjusting.py
import dateutil.parser
import csv

def parse_row(input_row, parsers):
    """wende je einen aus einer Liste von Parsern (dürfen auch None sein)
    auf jedes Element von input_row an"""
    return [try_or_none(parser)(value) if parser is not None else value
            for value, parser in zip(input_row, parsers)]

def parse_row_with(reader, parsers):
    """verpacke den reader, um die Parser auf jede Zeile anzuwenden"""
    for row in reader:
        yield parse_row(row, parsers)

def try_or_none(f):
    """liefert None, falls f einen Ausnahmefehler erzeugt
    nimmt an, dass f nur einen Eingabewert benötigt"""
    def f_or_none(x):
        try:
            return f(x)
        except:
            return None
    return f_or_none

def try_parse_field(field_name, value, parse_dict):
    """versuche, den Wert mit der Funktion aus parser_dict zu parsen"""
    parser = parser_dict.get(field_name) # None, falls kein Eintrag
    if parser is not None:
        return try_or_none(parser)(value)
    else:
        return value

def parse_dict(input_dict, parser_dict):
    return { field_name : try_parse_field(field_name, value, parser_dict)
             for field_name, value in input_dict.iteritems()}

data = []

with open("comma_delimited_stock_prices.csv", "rb") as f:
    reader = csv.reader(f)
    for line in parse_row_with(reader, [dateutil.parser.parse, None, float]):
        data.append(line)

for row in data:
    if any(x is None for x in row):
        print row
