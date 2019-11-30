from __future__ import unicode_literals
import docx
import ftfy
import sys
from bs4 import BeautifulSoup as bs
import requests
import os
import re
import time
# -*- coding: utf-8 -*-

# Quotes#Combat
# Quotes#Events

# CURR: Get doll url's from index page

# Extract weapon background, design, and trivia notes for English proofreading

library_page = "https://en.gfwiki.com/wiki/T-Doll_Index"
base_url = "https://en.gfwiki.com/wiki/"

def get_soup(url):
  headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
  html_page = requests.get(url, headers=headers)
  return bs(html_page.text, "html.parser")

# finds the card data from the inxed
def find_initial_data_from_soup(soup):
  # target class carrying key info inside is "card-bg-small" on this site
  all_span_cards = soup.find_all("span", class_="card-bg-small")
  return all_span_cards

# now we start extracting specific data from the html containing stuff we're interested in
def get_names_from_data(data_list):
  name_list = []
  # Can shorten data here if you [sl:ice] the data list!!!
  for x in data_list:
    name = x.find("span", class_="name").text
    name_list.append(name)
  return name_list

def generate_urls_from_names(name_list, base_url):
  character_urls = [] 
  for name in name_list:
    named_url = (base_url + name)
    character_urls.append(named_url)
  return character_urls

# Stuff for once you're on the character's webpage
# !!! Grab the weapon background from the base doll's page
def find_weapon_info(soup):
  wep_info = soup.find(text="Weapon Background").find_next(text="Weapon Background").find_next('p').text
  return wep_info

# get all text content until you run into an h2 tag
def find_design_info(soup):
  # try:
    #design_note is var for design info bits
    design_note = ""
    design_header = soup.find(id="Design")
    p1 = design_header.next_element.next_element.next_element
    design_note += p1.text
    cou = 0
    while True:
      next_tag_type = p1.next_element.name
      # end the loop when h2 is encountered
      if next_tag_type == "h2":
        # print("[+][+] --> h2 found! Ending design section search...")
        break
      elif next_tag_type == "p" or next_tag_type == "ul":
        # print("----- text content: " )
        txt_content = p1.next_element.text
        try:
          # get the text of the next element we're peeking at
          design_note += txt_content
        except:
          # if weird chars show up, just give me question marks
         txt_content = txt_content.encode('ascii', 'replace')
         design_note += txt_content
      elif cou >= 48:
        print("loop exceeded 48 runs")
        break
      # else:
        # print("ignored non-target tag...")
      # make current element the next element
      p1 = p1.next_element
      # bump up saftey net counter
      cou += 1
    return design_note

# find all <li> 's since the entire data set is contained in them
def find_trivia_info(soup):
  try:
    # trivia_bullets is list of all trivia text bits
    trivia_bullets = soup.find(id="Trivia").find_next('ul').find_all('li', recursive=False)
    trivia_paragraph = ""
    # all_trivia_list = []
    for x in trivia_bullets:
      bare_text = x.text.strip()
      try:
        trivia_paragraph += ("\t" + bare_text + '\n')
      # all_trivia_list.append(bare_text)
      # print(bare_text + "\n")
      except:
        bare_text = ("\t" + bare_text.encode('ascii', 'replace') + '\n')
        trivia_paragraph += bare_text
    # return all_trivia_list
    return trivia_paragraph
  except:
    return "no trivia details"

# def extract_char_info(soup):
#   x = find_weapon_info(soup)
#   y = find_design_info(soup)
#   z = find_trivia_info(soup)
#   return [x, y, z]
# Doll icon extaraction works, but I'm not using it for anything
# def get_doll_icon_src(data_list): 
#   doll_icon_list = []
#   for x in data_list[0:4]:
#     icon = x.find("img", class_="doll-image").get("src")
#     doll_icon_list.append(icon)
#   return doll_icon_list

# run that shit:
tdoll_index_soup = get_soup(library_page)
data_list = find_initial_data_from_soup(tdoll_index_soup)
# print("[ + ] added " + str(len(data_list)) + " items to index data array...")
# Add below dynamically to class
name_list = get_names_from_data(data_list)
# icon_list = get_doll_icon_src(data_list)
char_pg_urls = generate_urls_from_names(name_list, base_url)
# do the whole data-extraction gig in a for-each loop to go over all urls

# t1 = char_pg_urls[69]
t1 = "https://en.gfwiki.com/wiki/C96"

print("testing character url at:  -> " + t1)
test_soup = get_soup(t1)
# captured design in --> design_info_paragraph
design_info_paragraph = (find_design_info(test_soup))
trivia_paragraph = (find_trivia_info(test_soup))
print(design_info_paragraph)
# print(find_weapon_info(test_soup))

# print(find_weapon_info(test_soup))

# test_extraction = extract_char_info(test_soup)
# for x in test_extraction:
#   print(name_list[69] + "\n" + x)

# ////////////////

# #  find all images, extract to function
# # imgdata = {}
# # for img in soup.find_all('img'):
# #   imgdata[(img.get('src'))] = img.get('title')


# ///////////////////////////////////

# quotes_link = url + "/Quotes"
# # headers already declared at top of page
# q_html = requests.get(quotes_link, headers=headers)
# q_soup = bs(q_html.text, "html.parser")

# audio_source_list = []

# aud_tags = q_soup.select(".audio-button")
# for x in aud_tags:
#   audio_source_list.append(x.get("data-src"))

# gibberish_list = (q_soup.find_all(class_="audio-button"))

# japanese_text = []

# # Document() remains empty to make a new document, but needs the name called in "doc.save()" thereafter
# doc = docx.Document()

# doc.add_paragraph('Test from python placeholder 7')

# counter1 = 0
# for x in gibberish_list:
#   question_marks = x.parent.text
#   purified_line = ftfy.fix_encoding(question_marks)
#   # question_marks = x.parent.text.encode('ascii', 'replace')
#   # jpn_line = question_marks[0:-5]
#   # slice gets rid of "play" at the end of 'em all
#   jpn_line = purified_line[0:-5]
#   if jpn_line:
#     counter1 +=1
#     fixed_japanese = (ftfy.fix_text(jpn_line))
#     # doc.add_paragraph(fixed_japanese)
#     japanese_text.append(fixed_japanese)


# print(str(counter1) + " lines added to arr")
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

# class SoupExtractor:
#   def __init__(self, main_url):
#     self.main_url = main_url

# cob1 =  SoupExtractor("https://en.gfwiki.com/wiki/C96")
# cob1.main_soup = property(lambda self: get_soup(self.main_url))
# print(find_design_info(cob1.main_soup))

# things we want in our output document:
#  T-doll name : tdoll_name
# Japanese
# English
# audio link

# [[j1,e1,aud1],[j2,e2,aud2]...], char2: [[...]...]