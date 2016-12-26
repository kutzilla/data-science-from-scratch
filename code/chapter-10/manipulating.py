#!/usr/bin/env python
# -*- coding: utf-8 -*-
# manipulating.py
import datetime
from collections import defaultdict

def picker(field_name):
    """liefert eine Funktion, die ein Feld aus einem dict herauspickt"""
    return lambda row: row[field_name]

def pluck(field_name, rows):
    """wandle eine Liste von dicts in eine Liste von field_name-Werten um"""
    return map(picker(field_name), rows)

def group_by(grouper, rows, value_transform=None):
    # key ist die Ausgabe von grouper, value ist eine Liste von Zeilen
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)

    if value_transform is None:
        return grouped
    else:
        return { key : value_transform(rows)
                 for key, rows in grouped.iteritems()}

data = [
    {'closing_price' : 102.06,
     'date' : datetime.datetime(2014, 8, 29, 0, 0),
     'symbol' : 'AAPL'},
    {'closing_price' : 132.13,
     'date' : datetime.datetime(2015, 8, 29, 0, 0),
     'symbol' : 'AAPL'},
    {'closing_price' : 117.36,
     'date' : datetime.datetime(2014, 8, 30, 0, 0),
     'symbol' : 'MS'},
    {'closing_price' : 112.36,
     'date' : datetime.datetime(2015, 8, 30, 0, 0),
     'symbol' : 'MS'},
]

max_appl_price = max(row["closing_price"]
                     for row in data
                     if row["symbol"] == "AAPL")

print max_appl_price

# gruppiere Zeilen nach Kürzeln
by_symbol = defaultdict(list)

for row in data:
    by_symbol[row["symbol"]].append(row)

# das Maximum für jedes Kürzel über eine Dict Comprehension
max_price_by_symbol = { symbol : max(row["closing_price"]
                                     for row in grouped_row)
                        for symbol, grouped_row in by_symbol.iteritems()}

print max_price_by_symbol

max_price_by_symbol = group_by(picker("symbol"),
                               data,
                               lambda rows: max(pluck("closing_price", rows)))

print max_price_by_symbol

def percent_price_change(yesterday, today):
    return today["closing_price"] / yesterday["closing_price"] - 1

def day_over_day_changes(grouped_rows):
    # sortiere die Zahlen nach Datum
    ordered = sorted(grouped_rows, key = picker("date"))

    # zippe, um Paare aufeinanderfolgender Tage zu erhalten
    return [{ "symbol" : today["symbol"],
              "date" : today["date"],
              "change" : percent_price_change(yesterday, today) }
            for yesterday, today in zip(ordered, ordered[1:])]

# key ist das Aktiensymbol, value ist die Liste mit dicts der "Veränderung"
changes_by_symbol = group_by(picker("symbol"), data, day_over_day_changes)

# sammle alle "Veränderungs"-dicts in einer großen Liste
all_changes = [change
               for changes in changes_by_symbol.values()
               for change in changes]

print all_changes

min_pct_change = min(all_changes, key = picker("change"))

print min_pct_change

max_pct_change = max(all_changes, key = picker("change"))

print max_pct_change

def combine_pct_changes(pct_change1, pct_change2):
    return (1 + pct_change1) * (1 + pct_change2) - 1

def overall_change(changes):
    return reduce(combine_pct_changes, pluck("change", changes))

overall_change_by_month = group_by(lambda row: row['date'].month,
                                   all_changes,
                                   overall_change)

print overall_change_by_month
