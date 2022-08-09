#! /usr/bin/env python3

import os
import requests
import json

url = "http://34.71.68.179/fruits/"
file_path = "./supplier-data/descriptions/"
file_list = [file for file in os.listdir(file_path) if file.startswith('0')]

# Get information about previously uploaded items
res = requests.get(url)
posted = []
for items in res.json():
  posted.append(items['name'])

# Upload only new items
for file in file_list:
  payload = {}
  file_name, ext = os.path.splitext(file)
  with open(file_path + file, 'r') as  text:
    text_list = text.readlines()
    payload['name'] = text_list[0].strip('\n')
    payload['weight'] = int(text_list[1].strip('lbs \n'))
    payload['description'] = text_list[2].strip('\n')
    payload['image_name'] = file_name + ".jpeg"

  if payload['name'] in posted:
    print("{} was previously uploaded".format(payload['name']))
  else:
    response = requests.post(url,data=payload)
    if response.ok:
      print("Succesfully uploaded: ", payload['name'])