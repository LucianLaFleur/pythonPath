# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from bs4 import BeautifulSoup as bs
import requests
import os

# insert site url below
url = 'https://en.gfwiki.com/wiki/T-Doll_Index'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
html_page = requests.get(url, headers=headers)

soup = bs(html_page.text, "html.parser")

# imgdata = {}
# for img in soup.find_all('img'):
#   imgdata[(img.get('src'))] = img.get('title')

anchors = []
for a_tag_data in soup.find_all('a'):
  # linkpath = anchor.get('href')
  if a_tag_data.find('img'):
    if a_tag_data.get("title"):
      anchors.append(a_tag_data)
      
spider_strands = []
for a in anchors:
  # titles will be buggy with special chars like a backslash
  buggytitle = a.get('title')
  encodedtitle = buggytitle.encode('utf-8')
  spider_link = url + str(a.get('href'))
  print(encodedtitle)
  print(spider_link)
  # print(a.get('href'))
#   imgtag = a.get("img")
#   # tit = (a.get("title"))
#   # print(tit)
  print("-----------------")

# for i in imgdata:
#   # filter out captured images that have no tags, like banners
#   if imgdata[i] and imgdata[i][-4:] != "safe":
#     print(str(i) + "\n With data tags: \n " + str(imgdata[i]))
#     print("~~~   ~~~   ~~~   ~~~")

# 
#
# Save file as the tag list

