import re
# User input is obtained by [raw_input('prompt: )] in python 2.x
# x2 = raw_input('input x2')
# print(x2)
# x3 = raw_input('input x3')
# print(x3)

# x = "i3on34g/10"
# cutoff = x[:-2]
# new = cutoff + "9"
# print(new)

# create / generate range
# Use the range to iterate over different pages to run 2 - 13 automated instead of doing each by hand
#  .... .... . .. .. 
# list_2thru13 = range(2, 14)

# x.append("9")

# url = 'https://xxyyzz.org/1103211/9444ca87d5/?p=33'

#  find a string that returns a match
# x = int(re.findall("[^\D]*$", url)[0])
# y = x - 1
# print(y)

# Find all divs with something in it....
# all_divs = content_pg_soup.find_all("div")
# for div in all_divs:
#   title1 = div.get("title")
#   if title1 == "This alternative script was generated by a piece of software":
#     print(div)

#  Scan for all available links on page
# all_anchortags = content_pg_soup.find_all("a")
# counter2 = 0
# for anch in all_anchortags:
#   if anch.get("href"):
#     print("link at idx " + str(counter2) + ' ---  ' + anch.get("href"))
#     counter2 += 1

# extract unicode value from <title> tag
# \u672c\u65e5\u306f\u5b9a\u4f11\u65e5\u3067\u3059\u3002
# x1 = str((content_pg_soup.find_all('title')))
# uni_jp = re.findall("(u[^\s]*)", x1)[0]
# print(uni_jp)

# returning a string with python regex
# a = 'https://tatoeba.org//eng/sentences/show/195867'

# a2 = re.findall("[^\D]*$", a)[0]
# print(a2)

# beautiful soup find by attribute
# var111 = content_pg_soup.findall('div', lang="en")

# writing unicode chars to proper letter output in a word file

# doc = docx.Document()
# for jpn in furi_list:
  # purified_jpn = ftfy.fix_encoding(jpn)
  # fixed_jpn = ftfy.fix_text(purified_jpn)
  # doc.add_paragraph(purified_jpn)
# doc.save('jpTest4.docx')

# Purify mojibake with a given line variable: jpn_line
# purified_jpn = ftfy.fix_encoding(jpn_line)
# fixed_jpn = ftfy.fix_text(purified_jpn)

# make a list from a range ---
# list1 = range(2, 14)
# for y in list1:
#   print(y)