#!/usr/bin/env python

# read page html
# extract all links to a list

import requests
import re
import urlparse

target_url = "http://example.com"
target_links = []

def extract_links_from(url):
  response = requests.get(target_url)
  return href_links = re.findall("(?:href=\")(.*?)\"", response.content)

def crawl(url):
  href_links = extract_links_from(url)
  for link in href_links:
    # adds target url to the start of the relative path, parsing the url to do so
    link = urlparse.urljoin(url, link)
    # filter out external links by only including ones withing the target path

    if '#' in link:
      # store everything before the hash in the var
      # prevents page partials from repeating
      link = link.split('#')[0]

    # make sure the links don't repeat in the arr
    if target_url in link and link not in target_links:
      target_links.append(link)
      print(link)
      crawl(link)

crawl(target_url)