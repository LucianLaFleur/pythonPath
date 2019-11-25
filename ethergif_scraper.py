import sys
from bs4 import BeautifulSoup as bs
import requests
import os
import re
# -*- coding: utf-8 -*-

#Unknown why some gifs get "missed", could be a problem with irregular naming

scraped_gifs = []
current_pg = 0
lops = 0
max_page_idx = 0

def scrape_gogogo(url):
  headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
  html_page = requests.get(url, headers=headers)
  soup = bs(html_page.text, "html.parser")
# search for gifs along page and add them to scraped_gifs array
  for x in soup.findAll('img'):
    img_title = str(x.get("title"))
    # gif type targeted here
    if img_title[-4:] == ".gif":
      found_gif_link = x.parent.get("href")
      # add matching files to the ecraped gifs array
      scraped_gifs.append(found_gif_link)
  # finding the max number of pages
  if soup.find(class_="ptdd"):
    nav_l_arrow = soup.find(class_="ptdd")
    max_pg = nav_l_arrow.parent.contents[-2].text
    max_page_idx = int(max_pg) - 1
    print("max page is: " + str(max_page_idx))
    return max_page_idx
  elif soup.find(class_="ptds"):
    classed_nav_num = soup.find(class_="ptds")
    max_pg = classed_nav_num.parent.contents[-2].text
    max_page_idx = int(max_pg) - 1
    # print("(last pg idx is : " + str(max_page_idx) + ")")
    return max_page_idx
  else:
    print("Check: is the site one or two pages? use program variant")
    return 0
  

def get_url_nav(url, m_pg_idx):
  try:
    x = re.findall("[^\D]*$", url)[0]
    pg_num = int(x)
    if pg_num > 0:
      print("On page idx: " + str(pg_num) + " of " + str(m_pg_idx))
  except:
    print("On start page @ (0-idx)")

def open_giftab(choice):
  os.system("start " + scraped_gifs[choice])

def open_all_gifs():
  for gif in scraped_gifs:
    os.system("start " + gif)
  print(" --- [all scanned gifs opened in tabs]")

def browsing_loop(opts):
  while True:
    print("select: 0 - " + str(opts))
    # Get user input for what file to open, mod with os functionality
    browse_selection = raw_input('num/all opens tab, [c]an: ')
    if browse_selection == "c":
      print("browsing loop exited")
      break
    else:
      try:
        #  if input is within the acceptable option range...
        if browse_selection == "all":
          open_all_gifs()
        elif int(browse_selection) <= opts:
          print("idx# " + browse_selection + " opened")
          open_giftab(int(browse_selection))
        else:
          print("invalid num")
      except:
        print("input must be a num")

#  Reminder basic CLI syntax
# os.system("start " + x)

def scan_gifcount(link_options):
  if (link_options) >= 0:
    print("[+] --- " + str(link_options + 1) + " items found")
    # Calling the selection loop if gifs are found
    browsing_loop(link_options)
  else:
    print("[-] No gifs scanned on this page")

# CHECK NAVIGATION LOOP!@!#@! NEEX MAX CHECK
def fw(url):
  try:
    int(re.findall("[^\D]*$", url)[0])
    # the nums at the end of the url are in var end_nums
    end_nums = int(re.findall("[^\D]*$", url)[0])
    if end_nums <= max_page_idx:
      n_places = (len(str(end_nums)))
      return(url[:-(n_places)] + str(end_nums + 1))
    else:
      print("[- ] --- Already at max-idx page")
      return url
  except:
    return url + '?p=1'

def bk(url):
  try:
    t_int = int(re.findall("[^\D]*$", url)[0])
    if t_int == 1:
      return url[:-4]
    else:
      n_places = len(str(t_int))
      return(url[:-(n_places)] + str(t_int - 1))
  except:
      print("[-] Can't potato back")
      return(url)

def browse_scraped(url):
  scrape_gogogo(url)
  lops = (len(scraped_gifs) - 1)
  scan_gifcount(lops)
  # reset the gif arr
  del scraped_gifs [:]

def nav_loop(url, m_p_idx):
  while True:
    x = raw_input("PAGE NAVIGATION: [z] prev, ne[x]t, [c]ancel: \n")
    if x == "z" or x == "x" or x == "c":
      if x == "z":
        print(bk(url))
        browse_scraped((bk(url)))
        nav_loop(bk(url), m_p_idx)
      elif x == "x":
        print(fw(url))
        browse_scraped(fw(url))
        nav_loop(fw(url), m_p_idx)
      else:
        # implied, when raw_input is [c]... 
        print('backing out')
        break
      break
    else:
      print("invalid selection")

while True:
  url = raw_input("paste a url to scan: ")
  if url == "c":
   break
  else:
    max_page_idx = scrape_gogogo(url)
    # clear arr when multifunctional method is being used to get the max idx
    del scraped_gifs [:]
    get_url_nav(url, max_page_idx) 
    print("------------------")
    browse_scraped(url)
    nav_loop(url, max_page_idx)
  
# print("Reminder crtl+w closes current tab")
# again, "lops" are "link options" relating to indexes of the scraped gifs arr

# scan_gifcount(lops)