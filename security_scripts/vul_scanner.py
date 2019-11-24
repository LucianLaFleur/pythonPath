# !/usr/bin/env python
# How to vulnerability scanner:
# look across all pages
# look for ways to send data to web app (url, input forms, etc.)
# send payloads
# analyse payload response

import scanner

target_url = "http://123.45.6.44/example/path"
links_to_ignore = ["urls/to/ignore"]
# make a dictionary for accessable values so you can input data into the fields. 
# A brute-forcer can try different names and passwords, if none are extracted otherwise
data_dict = {"username": "admin", "password": "12345", "Login": "submit"}

vuln_scanner = scanner.Scanner(target_url)
# the "post" action allows you to send a post request with the dictionary k/v's what we set-up before.
vuln_scanner.session.post("http://url/path/here", data=data_dict)

vuln_scanner.crawl()

vuln_scanner.run_scanner()

# forms = vuln_scanner.extract_forms("http://target/url/path222")
# response = vuln_scanner.test_xss_in_form(forms[0], "http://target/url/path222" )
# to test in url:
# response = vuln_scanner.test_xss_in_link("target/url/here")
# print(response)