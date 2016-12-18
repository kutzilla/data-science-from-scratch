#!/usr/bin/env python
# -*- coding: utf-8 -*-
# twitter_stream_client.py
import json
from twython import TwythonStreamer


tweets = []

class MyStreamer(TwythonStreamer):
    """unsere Unterklasse von TwythonStreamer gibt an,
    wie wir mit dem Stream interagieren"""

    def on_success(self, data):
        """Was tun wir, wenn Twitter uns Daten schickt?
        hier sind die Daten ein Python dict pro Tweet"""

        # wir sind nur an Tweets auf Englisch interessiert
        if data['lang'] == 'en':
            tweets.append(data)
            print "received tweet #", len(tweets)

        # Stopp, wir haben genug gesammelt
        if len(tweets) >= 10:
            self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()

# liest die Datei credentials.json, welche die Zugangsdaten zur Twitter API
# beinhaltet. Die Datei ist durch die .gitignore vom Repository ausgeschlossen
with open('credentials.json') as credentials_file:
    credentials = json.load(credentials_file)

consumer_key = credentials["consumer_key"]
consumer_secret = credentials["consumer_secret"]
access_token = credentials["access_token"]
access_token_secret = credentials["access_token_secret"]

stream = MyStreamer(consumer_key, consumer_secret,
                    access_token, access_token_secret)

# sammelt öffentliche Statusmeldungen mit dem Schlüsselwort 'data'
stream.statuses.filter(track = 'data')

# wenn wir eine Stichprobe *aller* öffentlichen Meldungen möchten
# stream.statuses.sample()
