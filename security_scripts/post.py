#!/use/bin/env python
import requests

target_url = "example.com"
# last item in dictionary is the button for submitting
data_dict = {"username": "potato1", "password":"potato3", "Login":"submit"}

response = requests.post(target_url, data=data_dict)