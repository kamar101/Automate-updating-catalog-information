#!/usr/bin/env python3

from PIL import Image
import os


files_path = './supplier-data/images/'
files = [file for file in os.listdir(files_path) if file.startswith('0')]

for file in files:
  file_name, extension = os.path.splitext(file)
  if extension == '.tiff':
    with Image.open(files_path + file) as im:
      rgb_im = im.convert('RGB').resize((600,400))
      print('Converting: ', file)
      rgb_im.save(files_path + file_name + ".jpeg")
    print('Deleting file: ', file)
    os.remove(files_path + file)
  else:
    print('File alreday in .jpeg: ' , file)
