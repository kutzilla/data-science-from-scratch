#!/usr/bin/env python
# -*- coding: utf-8 -*-
# naive_bayes.py

from __future__ import division
from collections import defaultdict
from collections import Counter
import re
import random
import glob
import math

def split_data(data, prob):
    """teile die Daten in Fraktionen [prob, 1 - prob]"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def tokenize(message):
    message = message.lower()                        # Kleinbuchstaben
    all_words = re.findall("[a-z0-9']+", message)    # Wörter extrahieren
    return set(all_words)

def count_words(training_set):
    """Trainingsdatensatz enthält Paare (message, is_spam)"""
    counts = defaultdict(lambda: [0, 0])

    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1] += 1
    return counts

def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
    """wandle word_counts in eine Liste von Tripeln um
    w, p (w | spam) und p(w | ~spam)"""
    return [(w,
             (spam + k) / (total_spams + 2 * k),
             (non_spam + k) / (total_non_spams + 2 * k))
             for w, (spam, non_spam) in counts.iteritems()]

def spam_probability(word_probs, message):
    message_words = tokenize(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0

    # iteriere durch alle Wörter in Vokabular
    for word, prob_if_spam, prob_if_not_spam in word_probs:

        # wenn *word* in einer Nachricht vorkommt,
        # addiere die log-Wahrscheinlichkeit, es zu sehen
        if word in message_words:
            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)

        # wenn *word* nicht in der Nachricht vorkommt
        # addiere die log-Wahrscheinlichkeit, es _nicht_ zu Sonderzeichen
        # entspricht log(1 - Wahrscheinlichkeit, es zu sehen)
        else:
            log_prob_if_spam += math.log(1.0 - prob_if_spam)
            log_prob_if_spam += math.log(1.0 - prob_if_not_spam)

    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)

class NaiveBayesClassifier:

    def __init__(self, k=0.5):
        self.k = k
        self.word_probs = []

    def train(self, training_set):

        # zähle Spam- und Nicht-Spam-Nachrichten
        num_spams = len([is_spam
                         for message, is_spam in training_set
                         if is_spam])
        num_non_spams = len(training_set) - num_spams

        # schicke Trainingsdaten durch unsere "Pipeline"
        word_counts = count_words(training_set)
        self.word_probs = word_probabilities(word_counts,
                                             num_spams,
                                             num_non_spams,
                                             self.k)

    def classify(self, message):
        return spam_probability(self.word_probs, message)


# setzen Sie den Pfad auf Ihr Verzeichnis mit den Daten an
path = r"/Users/Matthias/Development/Code/Python/data-science-from-scratch/code/chapter-13/*/*"

data = []

# glob.glob liefert jeden Dateinamen, der zum Pfad mit Jokersymbolen passt
for fn in glob.glob(path):
    is_spam = "ham" not in fn

    with open(fn, 'r') as file:
        for line in file:
            if line.startswith("Subject:"):
                # entferne "Subject: " am Anfang und behalte den Rest
                subject = re.sub(r"^Subject: ", "", line).strip()
                data.append((subject, is_spam))


random.seed(0)      # damit Sie und ich eine identische Antwort erhalten
train_data, test_data = split_data(data, 0.75)

classifier = NaiveBayesClassifier()
classifier.train(train_data)

# Tripel (Betreff, Wert von is_spam, Spam-Wahrscheinlichkeit)
classified = [(subject, is_spam, classifier.classify(subject))
              for subject, is_spam in test_data]

# Annahme, dass spam_probability > 0.5 mit der Vorhersage von Spam korresporendiert
# zähle die Kombination von (Wert is_spam, Vorhersage is_spam)
counts = Counter((is_spam, spam_probability > 0.5)
                 for _, is_spam, spam_probability in classified)

print counts

# sortiere aufsteigend nach spam_probability
classified.sort(key=lambda row: row[2])

# die höchste Spam-Vorhersage unter den Nicht-Spams
spammiest_hams = filter(lambda row: not row[1], classified)[-5:]

# die niedrigste Spam-Vorhersage unter den tatsächlichen Spams
hammiest_spams = filter(lambda row: row[1], classified)[:5]


print spammiest_hams

print hammiest_spams


def p_spam_given_word(word_prob):
    """verwende Satz von Bayes, um p(Spam | Nachricht enthält Wort) zu berechnen"""

    # word_prob ist eines der Tripel aus word_probabilities
    word, prob_if_spam, prob_if_not_spam = word_prob
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)

words = sorted(classified.word_probs, key=p_spam_given_word)

spammiest_words = words[-5:]
hammiest_words = words[5:]
