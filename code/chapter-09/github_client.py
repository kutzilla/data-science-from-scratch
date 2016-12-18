#!/usr/bin/env python
# -*- coding: utf-8 -*-
# github_client.py
import requests, json

endpoint = "https://api.github.com/users/joelgrus/repos"

repos = json.loads(requests.get(endpoint).text)

from dateutil.parser import parse
from collections import Counter

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekdays_counts = Counter(date.weekday() for date in dates)

print month_counts
print weekdays_counts

last_5_repositories = sorted(repos,
                             key=lambda r: r ["created_at"],
                             reverse = True)[:5]

last_5_languages = [repo["language"] for repo in last_5_repositories]

print last_5_languages
