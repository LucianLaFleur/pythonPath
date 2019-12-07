import sys
from bs4 import BeautifulSoup as bs
import requests
import time
import docx
import ftfy

# idx_url is the hub page linking to all units of interest
idx_url = "https://kancolle.fandom.com/wiki/Ship"
baseurl = "https://kancolle.fandom.com"
# test url for single page
# url = "https://kancolle.fandom.com/wiki/Prinz_Eugen"

def get_soup(url):
  headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
  html_page = requests.get(url, headers=headers)
  return bs(html_page.text, "html.parser")

def get_tables(url):
  p_soup = get_soup(url)
  all_tables = p_soup.find_all("table", class_="wikitable")
  tar_tables = all_tables[0:3]
  return tar_tables

def get_url_and_name_arrays(idx_url):
  names_arr = []
  urls_arr = []
  idx_soup = get_soup(idx_url)
  # all_adv_tooltip_links = idx_soup.find_all("span")
  all_adv_tooltip_links = idx_soup.find_all("span", class_="advanced-tooltip")
  for x in all_adv_tooltip_links:
    names_arr.append(x.text)
  for x in all_adv_tooltip_links:
    urls_arr.append(x.find("a").get("href"))
  return [names_arr, urls_arr]

def get_auds_and_headers(p_soup):
  all_quotes = p_soup.find_all("tr", class_="shipquote")
  aud_arr = []
  for tag in all_quotes:
    aud_arr.append(tag.find("a").get("href"))
  header_arr = []
  for tag2 in all_quotes:
    # slice away "play " text with idx 5
    header_text = (tag2.find("td").text[5:].strip())
    header_arr.append("-----" + header_text + "-----")
  return [header_arr, aud_arr]

def get_j_lines(p_soup):
  jpn_arr = []
  all_j = p_soup.find_all("td", class_="shipquote-ja")
  for j_tag in all_j:
    jpn_arr.append(j_tag.text.strip())
  return jpn_arr

def get_en_lines(p_soup):
  en_arr = []
  all_en = p_soup.find_all("td", class_="shipquote-en")
  for en_tag in all_en:
    en_arr.append(en_tag.text.strip())
  return en_arr

def get_all_info(p_soup):
  temp = get_auds_and_headers(p_soup)
  headers = temp[0]
  auds = temp[1]
  j_lines = get_j_lines(p_soup)
  en_lines = get_en_lines(p_soup)
  return [headers, auds, j_lines, en_lines]

def crawl_across_urls(baseurl, unit_names, unit_urls):
  for x in range(0, len(unit_urls)):
    curr_url = (baseurl + unit_urls[x])
    curr_name = unit_names[x]
    print("[+] " + curr_name + " ---- ")
    p_soup = get_soup(curr_url)
    data_arr = get_all_info(p_soup)
    aligned_lines = zip(*data_arr)
    # personal preference for making filenames with underscore instead of space
    fn = curr_name.replace(" ", "_").replace("/", "_or_")
    # make new document for each unit
    doc1 = docx.Document()
    for n in range(0, len(data_arr[1])):
      for x in range(0, 4):
        pure_line = ftfy.fix_encoding(aligned_lines[n][x])
        fixed_line = ftfy.fix_text(pure_line)
        doc1.add_paragraph(fixed_line)
    doc1.save(fn + ".docx")

# Process execution ///////////////
names_and_urls = get_url_and_name_arrays(idx_url)
unit_names = names_and_urls[0]
unit_urls = names_and_urls[1]

# crawl_across_urls(baseurl, unit_names, unit_urls)

turl = "https://kancolle.fandom.com/wiki/Iowa"
p_soup = get_soup(turl)
data_arr = get_all_info(p_soup)

# NOTE: incomplete: use this conditional to ignore dumb shit
def check_quotelength(p_soup):
  all_quotes = p_soup.find_all("tr", class_="shipquote")
  for tag in all_quotes:
    if tag.find("td", colspan="2"):
      print("tard-span discovered")
      print(tag.text.strip())
      print("---")
    # aud_arr.append(tag.find("a").get("href"))
 

check_quotelength(p_soup)

# cou1 = 0
# for x in data_arr:
#   print(str(cou1) + ": --- " + str(len(data_arr[x])))
#   cou1 += 1

# aligned_lines = zip(*data_arr)
print("---")
print("[+] All data successfully grabbed!")

#  //// sample //////////
# url = "https://kancolle.fandom.com/wiki/Shimushu"
# url = "https://kancolle.fandom.com/wiki/Nagato"
# url = "https://kancolle.fandom.com/wiki/Warspite"
# url = "https://kancolle.fandom.com/wiki/Prinz_Eugen"
# tar_tables = get_tables(url)

# p_soup = get_soup(url)
# data_arr1 = get_all_info(p_soup)
# # write all data to doc here!!! ---------
# for x in data_arr1:
#   print(x[3].encode("ascii", "replace"))

# unit_file_name = "t1"
# doc1 = docx.Document()
# process_target_tables(tar_tables, doc1)
# doc1.save(unit_file_name + ".docx")

# //////////////

 # for y in range(0, len(data_arr[0])):
    #   for x in range(0, 4):
    #     print(data_arr[x][y].encode("ascii", "replace"))
    # e.g.
    # print(data_arr[3][-1])

# for x in test_urls:
#   n1, n2, n3 = x.partition('wiki/')
#   name = n3.replace("_", " ")
#   print(name + "\n---")