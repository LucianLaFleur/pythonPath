#  check if python 2 or 3 i think?

import requests
from bs4 import BeautifulSoup as bs
import os

# src img website
# moe corner of pinterest? maybe try pexels or gelbooru?
# below is an archive thread...
url = 'https://archived.moe/c/thread/3538224/'

# download page to parse it, using the above url var to "get" it
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all img tags (looks through html text grabbed in soup var above)
image_tags = soup.findAll('img')

# mkdir for target images
# !!!! need multiple directories for multiple genre-sets (mk new dir with a new colle)
if not os.path.exists('moe_models'):
  os.makedirs('moe_models')

# jump into the target image directory
os.chdir('moe_models')

# imagefile name variable
x = 0

# write images to dir
for image in image_tags:
  try:
    url = image['src']
    source = requests.get(url)
    if source.status_code == 200:
      # name creation statement below
      with open('model-' + str(x) + '.jpg', 'wb') as f:
        # write the content derived from the request to save the file
        f.write(requests.get(url).content)
        f.close()
        x += 1
  except:
    pass

