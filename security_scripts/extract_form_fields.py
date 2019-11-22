#!/usr/bin/env python

import requests
from BeautifulSoup import BeautifulSoup
import urlparse

def request(url):
  try: 
    return requests.get("http://" + url)
  except requests.exceptions.ConnectionError:
    pass

target_url = "example.com"
response = request(target_url)

parsed_html = BeautifulSoup(response.content)
# select all "form" fields from the html
forms_list = parsed_html.findAll("form")

for form in forms_list:
  action = form.get("action")
  # attatch the action to the url with parsing it and then joining
  post_url = urlparse.urljoin(target_url, action)
  method = form.get("method")

  inputs_list = form.findAll("input")
  post_data = {}
  for input in inputs_list:
    # extract the name value from the input fields
    input_name = input.get("name")
    input_type = input.get("type")
    input_value = input.get("value")
    if input_type == "text":
      input_value = "potato test"
    # assign the resulting input to the data dict. in a k/v pair
    post_data[input_name] = input_value
  result = requests.post(post_url, data=post_data)
  print(result.content)