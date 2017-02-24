#!/usr/bin/env python
# -*- coding: utf-8 -*-
# decision_trees.py
from __future__ import division
import math
from collections import Counter, defaultdict
from functools import partial

def entropy(class_probabilities):
        """Berechne die Entropie aus einer Liste von Klassenwahrscheinlichkeiten"""
        return sum(-p * math.log(p, 2)
                   for p in class_probabilities
                   if p)                        # ignoriere Wahrscheinlichkeit null

def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count
            for count in Counter(labels).values()]

def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
    """berechne die Entropie dieser Partition der Daten in Untermengen
    subsets ist eine verschachtelte Liste annotierter Daten"""

    total_count = sum(len(subset) for subset in subsets)

    return sum(data_entropy(subset) * len(subset) / total_count
               for subset in subsets)

def partition_by(inputs, attribute):
    """jede Eingabe ist ein Paar (attribute_dict, label).
    ergibt ein dict : attribute_value -> inputs"""
    groups = defaultdict(list)
    for input in inputs:
        key = input[0][attribute]   # nimm den Wert des angegebenen Attributs
        groups[key].append(input)   # füge die Eingabe zu den korrekten hinzu
    return groups

def partition_entropy_by(inputs, attribute):
    """berechnet die Entropie für die gegebene Partition"""
    partitions = partition_by(inputs, attribute)
    return partition_entropy(partitions.values())

def classify(tree, input):
    """klassifiziere die Eingabe mit dem gegebenen Entscheidungsbaum"""

    # wenn dies ein Blatt ist, gib dessen Wert zurück
    if tree in [True, False]:
        return tree

    # anderenfalls enthält der Baum ein Attribut für die Zerlegung
    # und ein Dictionary mit den Werten des Attributs als Schlüssel
    # und den zu betrachteten Unterbäumen als Werte
    attribute, subtree_dict = tree

    subtree_key = input.get(attribute)  # None, falls das Attribut fehlt

    if subtree_key not in subtree_dict: # wenn es für key keinen Unterbaum gibt,
        subtree_key = None              # verwende den Unterbaum für None

    subtree = subtree_dict[subtree_key] # wähle den entsprechenden Unterbaum
    return classify(subtree, input)     # und verwende ihn um Klassifizieren
                                        # der Eingabe

def build_tree_id3(inputs, split_candidates=None):

    # im ersten Durchgang sind alle Schlüssel
    # der ersten Eingabe mögliche Zerlegungen
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()

    # zähle True und False in den Eingabedaten
    num_inputs = len(inputs)
    num_trues = len([label for item, label in inputs if label])
    num_false = num_inputs - num_trues

    if num_trues == 0: return False     # kein True? Gib ein Blatt mit "False"
                                        # zurück
    if num_false == 0: return True      # kein False? Gib ein Blatt mit "True"
                                        # zurück

    if not split_candidates:            # falls keine möglichen Zerlegungen übrig sind
        return num_trues >= num_false   # bestimmt die Mehrheit das Blatt

    # anderenfalls zerlege am besten Attribut
    best_attribute = min(split_candidates,
                         key=partial(partition_entropy_by, inputs))

    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in split_candidates
                      if a != best_attribute]

    # baue die Unterbäume rekursiv auf
    subtrees = { attribute_value : build_tree_id3(subset, new_candidates)
                 for attribute_value, subset in partitions.iteritems()}

    subtrees[None] = num_trues > num_false  # Standardwert

    return (best_attribute, subtrees)

def forest_classify(trees, input):
    votes = [classify(tree, input) fpr tree in trees]
    vote_counts = Counter(votes)
    return vote_counts.most_common(1)[0][0]

if __name__ == "__main__":

    inputs = [
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},   False),
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'yes'},  False),
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'no'},     True),
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'no'},  True),
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'yes'},    False),
        ({'level':'Mid','lang':'R','tweets':'yes','phd':'yes'},        True),
        ({'level':'Senior','lang':'Python','tweets':'no','phd':'no'}, False),
        ({'level':'Senior','lang':'R','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'Python','tweets':'yes','phd':'no'}, True),
        ({'level':'Senior','lang':'Python','tweets':'yes','phd':'yes'},True),
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'yes'},    True),
        ({'level':'Mid','lang':'Java','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'yes'},False)
    ]

    for key in ["level", "lang", "tweets", "phd"]:
        print key, partition_entropy_by(inputs, key)

    senior_inputs = [(input, label)
                     for input, label in inputs if input["level"] == "Senior"]

    for key in ["lang", "tweets", "phd"]:
        print key, partition_entropy_by(senior_inputs, key)

    tree = build_tree_id3(inputs)

    print classify(tree, {'level':'Junior','lang':'Java','tweets':'yes','phd':'no'})
    print classify(tree, {'level':'Junior','lang':'Java','tweets':'yes','phd':'yes'})
    print classify(tree, {'level':'Intern'})
    print classify(tree, {'level':'Senior'})
