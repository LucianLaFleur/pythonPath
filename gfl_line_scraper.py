from __future__ import unicode_literals
import docx
import ftfy
import sys
import codecs
from bs4 import BeautifulSoup as bs
import requests
import os
import re
# -*- coding: utf-8 -*-

# insert site url below
# for weapon info extraction : https://en.gfwiki.com/wiki/M500
# quote extraction, obviously: https://en.gfwiki.com/wiki/M500/Quotes
url = 'https://en.gfwiki.com/wiki/MAC-10'

headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}

html_page = requests.get(url, headers=headers)

soup = bs(html_page.text, "html.parser")

# extract the character's name from the wiki page
notimportant1, notimportant2, tdoll_name = url.partition("wiki/")

# imgdata = {}
# for img in soup.find_all('img'):
#   imgdata[(img.get('src'))] = img.get('title')

paragraphs = []

for p_tag_data in soup.find_all('p'):
  paragraphs.append(p_tag_data)

# for x in paragraphs:
#   print(x)

# !!! Grabs the weapon background from the base doll's page
# Call find next twice to get second instance of this text line because the first is a nav link, the second is the target header
wep_bg_p = soup.find(text="Weapon Background").find_next(text="Weapon Background").find_next('p').contents[0]

# print(wep_bg_p)

# ///////////////////////////////////

quotes_link = url + "/Quotes"
# headers already declared at top of page
q_html = requests.get(quotes_link, headers=headers)
q_soup = bs(q_html.text, "html.parser")

audio_source_list = []

aud_tags = q_soup.select(".audio-button")
for x in aud_tags:
  audio_source_list.append(x.get("data-src"))

gibberish_list = (q_soup.find_all(class_="audio-button"))

japanese_text = []

# Document() remains empty to make a new document, but needs the name called in "doc.save()" thereafter
doc = docx.Document()

doc.add_paragraph('Test from python placeholder 7')

counter1 = 0
for x in gibberish_list:
  question_marks = x.parent.text
  purified_line = ftfy.fix_encoding(question_marks)
  # question_marks = x.parent.text.encode('ascii', 'replace')
  # jpn_line = question_marks[0:-5]
  jpn_line = purified_line[0:-5]
  if jpn_line:
    counter1 +=1
    fixed_japanese = (ftfy.fix_text(jpn_line))
    # doc.add_paragraph(fixed_japanese)
    japanese_text.append(fixed_japanese)


print(str(counter1) + " lines added to arr")
# doc.save('t777.docx')

# table_data = (q_soup.find_all("td"))
# for x in table_data:
#   x = x.encode('utf-8')
#   print(x)
#   print("--- --- --- ---")

# from bs4 import BeautifulSoup
# html = open("medium.html").read()
# soup = BeautifulSoup(html)
# tag = soup.find("div", text="inner")
# print tag.find_parent('div')
# OUTPUT
# <div>middle
#       <div>inner</div>
# </div>

# print(audio_source_list)

# spider_strands = []
# for a in anchors:
#   # titles will be buggy with special chars like a backslash
#   buggytitle = a.get('title')
#   encodedtitle = buggytitle.encode('utf-8')
#   spider_link = url + str(a.get('href'))
#   print(encodedtitle)
#   print(spider_link)
#   # print(a.get('href'))
# #   imgtag = a.get("img")
# #   # tit = (a.get("title"))
# #   # print(tit)
#   print("-----------------")

# for i in imgdata:
#   # filter out captured images that have no tags, like banners
#   if imgdata[i] and imgdata[i][-4:] != "safe":
#     print(str(i) + "\n With data tags: \n " + str(imgdata[i]))
#     print("~~~   ~~~   ~~~   ~~~")

# 
#
# Save file as the tag list

# things we want in our output document:
#  T-doll name : tdoll_name
# Japanese
# English
# audio link

# [[j1,e1,aud1],[j2,e2,aud2]...], char2: [[...]...]