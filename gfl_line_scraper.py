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

library_page = "https://en.gfwiki.com/wiki/T-Doll_Index"
base_url = "https://en.gfwiki.com/wiki/"
src_root = "https://en.gfwiki.com/"

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

def find_weapon_info(soup):
  try:
    wep_note = ""
    info1 = soup.find(text="Weapon Background").find_next(text="Weapon Background").find_next('p')
    wep_note += ("\t" + info1.text)
    cou = 0
    while True:
      next_tag_type = info1.next_element.name
      # end the loop when h2 is encountered
      if next_tag_type == "h2":
        # print("[+][+] --> h2 found! Ending design section search...")
        break
      # Will grab text from any p or ul elements
      elif next_tag_type == "p" or next_tag_type == "ul":
        txt_content = info1.next_element.text
        try:
          # get the text of the next element we're peeking at
          wep_note += ("\t" + txt_content)
        except:
          # if weird chars show up, just give me question marks
          txt_content = txt_content.encode('ascii', 'replace')
          wep_note += ("\t" + txt_content)
      elif cou >= 40:
        print("Weapon info loop exceeded 40 runs")
        break
      # else:
        # print("ignored non-target tag...")
      # make current element the next element
      info1 = info1.next_element
      # bump up saftey net counter
      cou += 1
  except:
    return "[-] No weapon details"
  return wep_note

# get all text content until you run into an h2 tag
def find_design_info(soup):
  try:
    #design_note is var for design info bits
    design_note = ""
    design_header = soup.find(id="Design")
    p1 = design_header.next_element.next_element.next_element
    design_note += ("\t" + p1.text)
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
          design_note += ("\t" + txt_content)
        except:
          # if weird chars show up, just give me question marks
         txt_content = txt_content.encode('ascii', 'replace')
         design_note += ("\t" + txt_content)
      elif cou >= 48:
        print("Loop exceeded 48 runs")
        break
      # make current element the next element
      p1 = p1.next_element
      cou += 1
  except:
    return "[-] No design details"
  return design_note

# find all <li> 's since the entire data set is contained in them
def find_trivia_info(soup):
  try:
    # trivia_bullets is list of all trivia text bits
    trivia_bullets = soup.find(id="Trivia").find_next('ul').find_all('li', recursive=False)
    trivia_paragraph = ""
    # all_trivia_list = []
    for x in trivia_bullets:
      bare_text = x.text
      try:
        trivia_paragraph += ("\t" + bare_text)
      # all_trivia_list.append(bare_text)
      # print(bare_text + "\n")
      except:
        bare_text = ("\t" + bare_text.encode('ascii', 'replace'))
        trivia_paragraph += bare_text
    # return all_trivia_list
    return trivia_paragraph
  except:
    return "[-] No trivia details"

# Search all info units on the soup for the char's homepage
def extract_char_info(soup):
  x = find_weapon_info(soup)
  y = find_design_info(soup)
  z = find_trivia_info(soup)
  suite = ("---weapon design ---\n" + x + "\n --- Char design/attire --- \n" + y + "\n --- Trivia Bullets --- \n" + z).encode('ascii', 'replace')
  # NOTE: purifying mojibake??
  return suite
  # returns a paragraph-long string

# Doll icon extaraction works, but I'm not using it for anything
# def get_doll_icon_src(data_list): 
#   doll_icon_list = []
#   for x in data_list[0:4]:
#     icon = x.find("img", class_="doll-image").get("src")
#     doll_icon_list.append(icon)
#   return doll_icon_list

# //// info extraction portion and method execution
tdoll_index_soup = get_soup(library_page)
data_list = find_initial_data_from_soup(tdoll_index_soup)
# print("[ + ] added " + str(len(data_list)) + " items to index data array...")
# Add below dynamically to class
name_list = get_names_from_data(data_list)
# icon_list = get_doll_icon_src(data_list)
char_pg_urls = generate_urls_from_names(name_list, base_url)
# do the whole data-extraction gig in a for-each loop to go over all urls

# t1 = char_pg_urls[9]
# mod3 included
t1 = "https://en.gfwiki.com/wiki/M4_SOPMOD_II"
# irregular, limited info, but normal num of tables, just some are absent content:
# t1 = "https://en.gfwiki.com/wiki/Jill"
# t1 = "https://en.gfwiki.com/wiki/C96"

print("testing character url at:  -> " + t1)
test_soup = get_soup(t1)
# print("Processing character info...")
char_info_suite = extract_char_info(test_soup)
# NOTE: be sure to purify mojibake before printing the char_info_suite to a document, as the odd chars are currently ?'s
test_quote_url = (t1 + "/Quotes")
t1_quote_soup = get_soup(test_quote_url)

all_tbody_tags = t1_quote_soup.find_all("tbody")

if len(all_tbody_tags) == 4:
  # print("Regular quotes found")
  general_quotes = all_tbody_tags[1]
  combat_quotes = all_tbody_tags[2]
  event_quotes = all_tbody_tags[3]
# Make exception for additional tables for MOD3
elif len(all_tbody_tags) == 7:
  # print("Mod3 quotes found")
  general_quotes = all_tbody_tags[1]
  combat_quotes = all_tbody_tags[2]
  event_quotes = all_tbody_tags[3]
  mod3_general_quotes = all_tbody_tags[4]
  mod3_combat_quotes = all_tbody_tags[5]
  mod3_event_quotes = all_tbody_tags[6]
else:
  print("Irregular num of quote tables for " + t1)

# idx 0 should be title, 2 -> Japanese, 4 -> English
# <tr>
# <td style="background:rgba(0, 0, 0, 0.6)">Acquisition
# </td>
# <td style="background:rgba(0, 0, 0, 0.6)">???
# </td>
# <td style="background:rgba(0, 0, 0, 0.6)">???<span class="audio-button" data-src="https://en.gfwiki.com/images/f/f8/C96_GAIN_JP.ogg" style="display:block"><a href="/wiki/File:C96_GAIN_JP.ogg" title="File:C96 GAIN JP.ogg">Play</a></span>
# </td>
# <td style="background:rgba(0, 0, 0, 0.6)">???
# </td>
# <td style="background:rgba(0, 0, 0, 0.6)">You're my Commander, aren't you? </td></tr>


gen_rows = general_quotes.find_all('tr')
# remove junk data in 0 idx row
del gen_rows[0]

# NOTE: [  :::  ] incomplete [  :::  ]
# ENCAPSULATE: for each item in the row table, extract row data and the audio
# for each row in range(0, len(gen_rows))

# get all the table-data from within the row
rd_list = gen_rows[0].find_all("td")

# belowgets the audio src
aud_href = gen_rows[4].find("a", text="Play").get("href")
if aud_href:
  aud_src = src_root + aud_href
else:
  aud_src = "No audio available"

# UNUSED, not needed as title is in audiofile name ; checks for row title
# if rd_list[0].text.strip():
#   title_rd = rd_list[0].text.strip()
# else:
#   print("No title found")
#   title_rd = "untitled row"

# check for JPN content
if rd_list[2].text.strip():
  jpn_rd = rd_list[2].text.strip()
  # slice out the unneeded "play" text that appears
  jpn_rd = jpn_rd[:-4]
else:
  print("No Jpn text found")
  jpn_rd = "[-] No Jpn"

# check for English content
if rd_list[4].text.strip():
  eng_rd = rd_list[4].text.strip()
else:
  print("No Eng text found")
  end_rd = "[-] No Eng"

print("testing extracted vals")
print("---")
time.sleep(1)
#Title, Japanese, and translation successfully extracted!
extracted_rd = [aud_src, jpn_rd, eng_rd]
for x in extracted_rd:
  print(x.encode('ascii', 'replace'))
  print("~~~")


# for x in gen_rows:
#   try:
#     print(x)
#     print("---   end of row " + str(gr_idx) + " ---")
#   except:
#     print("skipped unprintible chars")
#   gr_idx += 1

# ///////////////////////////////////

# quotes_link = url + "/Quotes"
# # headers already declared at top of page
# q_html = requests.get(quotes_link, headers=headers)
# q_soup = bs(q_html.text, "html.parser")

# audio_source_list = []
# aud_tags = q_soup.select(".audio-button")
# for x in aud_tags:
#   audio_source_list.append(x.get("data-src"))
# print(audio_source_list)

# NOTE: purifying mojibake
# doc = docx.Document()
# for jpn in furi_list:
  # purified_jpn = ftfy.fix_encoding(jpn)
  # fixed_jpn = ftfy.fix_text(purified_jpn)
  # doc.add_paragraph(purified_jpn)
# doc.save('jpTest4.docx')

# Purify mojibake with a given line variable: jpn_line
# purified_jpn = ftfy.fix_encoding(jpn_line)
# fixed_jpn = ftfy.fix_text(purified_jpn)

# NOTE: .encode('utf-8') might be necessary if the doll's name has a weird char or backslash in their name...
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