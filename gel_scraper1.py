# import requests
from bs4 import BeautifulSoup as bs
import urllib2
import os

# Scrape only "safe" images from Gelbooru's site

# insert site url below

html_page = urllib2.urlopen("https://gelbooru.com/index.php?page=post&s=list&tags=j%40ck")

# grab the page data with "get"
# resp = requests.get(url)
# soup = bs(resp.text, 'html.parser')
soup = bs(html_page, "html.parser")

imgdata = {}
for img in soup.find_all('img'):
  imgdata[(img.get('src'))] = img.get('title')

# init list placeholder
# images = []
# taglist placeholder
# taglist = []

# for img in soup.find_all('img'):
#   images.append((img.get('src')))
#   taglist.append((img.get('title')))

# DOCUMENTATION: first two images are for banner setups.
# need to ignore the first two data sources and the last one

# weeded_images = imgdata[2:-1]

# for x in weeded_images:
#   print(x)
#   print("~~~ ~~~ ~~~ ~~~")

for i in imgdata:
  # filter out captured images that have no tags, like banners
  if imgdata[i] and imgdata[i][-4:] == "safe":
    print(str(i) + "\n With data tags: \n " + str(imgdata[i]))
    print("~~~   ~~~   ~~~   ~~~")

# print('img data sucessfully extracted')

# target_info = soup.select("img")
# for thing in target_info:
#   print(thing.text.strip())

# 
#
# Save file as the tag list

