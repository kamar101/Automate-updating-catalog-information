#!/usr/bin/env python3

import reports
import os
import requests
from datetime import date
import emails

# Get current date and develop pdf title
day = date.today()
title = "Processed Update on {0:%B} {0:%d}, {0:%Y}".format(day)


# file location and new pdf attachment path
attachment = "/tmp/processed.pdf"
file_path = "./supplier-data/descriptions/"
file_list = [file for file in os.listdir(file_path) if file.startswith('0')]
info_dict = {}

# iterate over each files and add required values into a dictionary
for files in file_list:
  with open(file_path + files, 'r') as text:
    text_list = text.readlines()
    name = text_list[0].strip('\n')
    weight = text_list[1].strip('\n')
    info_dict[name] = weight

# Create a new list and append formated string
info_list = []
for name,weight in info_dict.items():
  formated = "name: {} <br/> weight: {}".format(name,weight)
  info_list.append(formated)
  info_list.append("")

# Get email information
sender = 'automation@example.com'
recepiant = "student-02-33e3f680c1fb@example.com"
subject = "Upload Completed - Online Fruit Store"
body = " All fruits are uploaded to our website successfully. A detailed list is attached to this email"
attachment = "/tmp/processed.pdf"

if __name__ == "__main__":
  report_body = "<br/>".join(info_list)
  reports.generate_report(attachment,title,report_body)
  message = emails.generate_email(sender,recepiant,subject,body,attachment)
  emails.send_email(message)
  print('done')