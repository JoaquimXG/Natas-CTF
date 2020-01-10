#!/bin/python3

import requests
import re
import html.parser

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
secret = "oubWYf2kBq" #gained from reversing the function in 8.php

url = 'http://%s.natas.labs.overthewire.org' % (username)
data = { "secret" : "oubWYf2kBq" ,"submit" : "submit" }

#for communicating with the website whilst maintaining session history
session = requests.Session()
response = session.post(url + '',data = data, auth = (username,password) )
content = html.unescape(response.text)

#for viewing the webpage
#print (content)

#for finding the password 
print (re.findall('ccess granted. The password for natas9 is (.*)',content)[0])



#------------------------------------------------------------------------------
#the encoding function
#bin2hex(strrev(base64_encode($secret)))
#the encoded result
#3d3d516343746d4d6d6c315669563362

#goal is to reverse the function


