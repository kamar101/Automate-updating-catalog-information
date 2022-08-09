#!/usr/bin/env python3

import os
import requests

url = "http://35.232.194.111/upload/"
file_path = "./supplier-data/images/"
files = [files for files in os.listdir(file_path) if files.startswith('0')]

for file in files:
  with open(file_path + file, 'rb') as im:
    response = requests.post(url, files = {'file': im})
  if response.status_code == 201:
    print("Succesfully uploaded: ", file)


