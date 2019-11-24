# !/usr/bin/env python

import urlparse
import requests
import re
from BeautifulSoup import BeautifulSoup

class Scanner:
  def __init__(self, url, ignore_links):
    # set up a session so you can send/recieve requests like get and post
    self.session = requests.Session()
    self.target_url = url
    self.target_links = []
    self.links_to_ignore = ignore_links
    
  def extract_links_from(self, url):
    response = self.session.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

  def crawl(self, url=None):

    # since this is recursively calling itself with self.crawl, this only needs the target url the first time it runs, then it'll spider out from there
    if url == None:
      url = self.target_url
    href_links = extract_links_from(url)
    for link in href_links:
      # adds target url to the start of the relative path, parsing the url to do so
      link = urlparse.urljoin(url, link)
      # filter out external links by only including ones withing the target path

      if '#' in link:
        # store everything before the hash in the var
        # prevents page partials from repeating
        link = link.split('#')[0]

      # make sure the links don't repeat in the arr
      if self.target_url in link and link not in target_links and link not in self.links_to_ignore:
        self.target_links.append(link)
        print(link)
        self.crawl(link)

  def extract_forms(self, url):
    response = self.session.fet(url)
    parsed_html = BeautifulSoup(response.content)
    forms_list = parsed_html.findAll("form")

  def submit_form(self, form, value, url)
    action = form.get("action")
    # attatch the action to the url with parsing it and then joining
    post_url = urlparse.urljoin(url, action)
    method = form.get("method")

    inputs_list = form.findAll("input")
    post_data = {}
    for input in inputs_list:
      # extract the name value from the input fields
      input_name = input.get("name")
      input_type = input.get("type")
      input_value = input.get("value")
      if input_type == "text":
        # assign sent value to the val param plugged into the method
        input_value =  value
      # assign the resulting input to the data dict. in a k/v pair
      post_data[input_name] = input_value
    result = self.session.post(post_url, data=post_data)
    return self.session.get(post_url, params=post_data)

    def run_scanner(self):
      for link in self.target_links:
        forms = self.extract_forms(link)
        for form in forms:
          # testing....
          is_vulnerable_to_xss = self.test_xss_in_form(form, link)
          if is_vulnerable_to_xss:
            print("XSS vulnerability discovered in " + link + "in")
            print(form)
        if "=" in link:
          is_vulnerable_to_xss = self.test_xss_in_link(link)
          if is_vulnerable_to_xss:
            print("XSS URL vulnerability detected in " + link)
          #  test 2  
  def test_xss_in_link(self, url):
    # insert test script in tags below
    xss_test_script = "<scriPt></sCript>"
    response = self.submit_form(form, xss_test_script, url)
    # shorthand for below, give True if the script makes it into the content
    return xss_test_script in response.content
    # if xss_test_script in response.content:
    #   return True

    def test_xss_in_form(self, form, url):
      # modify script below with JS or a call to a js file
      xss_test_script = "<scRiPt>myFunction()</sCrIpt>"
      response = self.submit_form(form, xss_test_script, url)
      # If the XSS worked, then the HTML will be modified in the response of the page
      if xss_test_script in response.content:
        return True

# outside of class now

# XSS cross site scripting:
# "persistent" is saved
#  "reflected" manipulates a URL that executes code
# "DOM-based" gets interpreted and run without interacting with the database
#  ----XSS examples: injecting into forms, injecting into urls