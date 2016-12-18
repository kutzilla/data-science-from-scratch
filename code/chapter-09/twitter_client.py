#!/usr/bin/env python
# -*- coding: utf-8 -*-
# twitter_client.py
import json
from twython import Twython

# liest die Datei credentials.json, welche die Zugangsdaten zur Twitter API
# beinhaltet. Die Datei ist durch die .gitignore vom Repository ausgeschlossen
with open('credentials.json') as credentials_file:
    credentials = json.load(credentials_file)

consumer_key = credentials["consumer_key"]
consumer_secret = credentials["consumer_secret"]

twitter = Twython(consumer_key, consumer_secret)


# suche nach Tweets mit der Wortfolge "data sciene"
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"].encode('utf-8')
    text = status["text"].encode('utf-8')
    print user, ":", text
    print
