import sys
from bs4 import BeautifulSoup as bs
import requests
import time
import docx
import ftfy

url = "https://kancolle.fandom.com/wiki/Prinz_Eugen"

def get_soup(url):
  headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
  html_page = requests.get(url, headers=headers)
  return bs(html_page.text, "html.parser")

def get_tables(url):
  p_soup = get_soup(url)
  all_tables = p_soup.find_all("table", class_="wikitable")
  tar_tables = all_tables[0:3]
  return tar_tables

def process_row_info(rowdata, n):
  tar_info = []
  # slice out this annoying "play" that's in the inner text of the audio button
  print("current iter is ... : " + str(n))
  if n == 2:
    tar_info.append("----- "+ rowdata[0].text.strip() +" -----")
  else:
    tar_info.append("----- "+ rowdata[0].text[5:].strip() +" -----")
  try:
    # audlink = rowdata[0].find("a").get("href")
    audlink = rowdata[0].find_all("a", text="Play")[0].get("href")
  except:
    audlink = "[-] no audio"
  tar_info.append(audlink)
  try:
    tar_info.append(rowdata[1].text.strip())
    # get English text
    tar_info.append(rowdata[2].text.strip())
  except:
    pass
  return tar_info


def process_target_tables(tar_tables, doc):
  # only the first 3 tables are of interest
  for x in range(0, 3):
    tablenum = x
    tr_list = tar_tables[x].find_all("tr")
    # tr_list[0] is just the column headers... can be ignored
    print("--- Row list length :" + str(len(tr_list)))
    # time.sleep(1)
    for y in range(1, len(tr_list)):
      curr_rowdata = tr_list[y].find_all("td")
      tar_info = process_row_info(curr_rowdata, tablenum)

  # exceptions for wonky seasonal table
  # if any of these trigger, it's an empty data thing to be ignored
      try:
        if (tar_info[1].strip()) == "":
          pass
          # print("Detected nothing at idx 1!")
        elif (tar_info[2].strip()) == "":
          pass
          # print("Detected nothing at idx 2!")
        elif (tar_info[3].strip()) == "":
          pass
          # print("Detected nothing at idx 3!")
        else:
          for z in tar_info:
            try:
              purified_line = ftfy.fix_encoding(z)
              fixed_line = ftfy.fix_text(purified_line)
              doc.add_paragraph(fixed_line)
              # print(x.encode("ascii", "replace"))
              # run printing operation here
            except:
              print("Check for line info processing error...")
              time.sleep(1)
      except:
        pass
        # print("Empty set skipped")

# ///////////////////////
# NOTE: make a bigger array and append all trs to it to iterate through them all
tar_tables = get_tables(url)
print("number of tables = "+ str(len(tar_tables)))

unit_file_name = "Prinz Eugen3"
doc1 = docx.Document()
process_target_tables(tar_tables, doc1)
doc1.save(unit_file_name + ".docx")

# //////////////

# find ship name from their url page
# test_urls = ["https://kancolle.fandom.com/wiki/Prinz_Eugen",
# "https://kancolle.fandom.com/wiki/Nagato",
# "https://kancolle.fandom.com/wiki/Mutsu"]

# for x in test_urls:
#   n1, n2, n3 = x.partition('wiki/')
#   name = n3.replace("_", " ")
#   print(name + "\n---")