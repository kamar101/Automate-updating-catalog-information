#!/usr/bin/env python3

import psutil
import socket
import emails

cpu_util = psutil.cpu_percent()
disk_util = psutil.disk_usage('/')[3]
memory_util = psutil.virtual_memory()[1]/1000000
dns_resolve = socket.gethostbyname('localhost')

sender = "automation@example.com"
recepiant = "student-02-33e3f680c1fb@example.com"
body = "Please check your system and resolve the issue as soon as possible"
subjects = ["Error - CPU usage is over 80%","Error - Available disk space is less than 20%","Error - Available memory is less than 500MB","Error - localhost cannot be resolved to 127.0.0.1"]

if cpu_util > 80:
  message = emails.generate_email(sender,recepiant,subjects[0],body)
  emails.send_email(message)
  print('Sent CPU Error Email')
elif disk_util < 20:
  message = emails.generate_email(sender,recepiant,subjects[1],body)
  emails.send_email(message)
  print('Sent Disk space Error Email')
elif int(memory_util)  < 500:
  message = emails.generate_email(sender,recepiant,subjects[2],body)
  emails.send_email(message)
  print('Sent Memory space Error Email')
elif dns_resolve != '127.0.01':
  message = emails.generate_email(sender,recepiant,subjects[3],body)
  emails.send_email(message)
  print('Sent localhost Error Email')

