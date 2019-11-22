#!/usr/bin/env python

import requests



# tests if a subdomain exists on website or not

def request(url):
  try: 
    return requests.get("http://" + url)
  except requests.exceptions.ConnectionError:
    pass

target_url = "example.com"

with open("/path/to/subdomains.list", "r") as wordlist_file:
  for line in wordlist_file:
    # gets rid of whitespace if words are each on their own line
    whitespace_stripped_word = line.strip()
    test_url = whitespace_stripped_word + "." + target_url
    resp = request(test_url)
    if resp:
      print("subdomain detected --> " + test_url)