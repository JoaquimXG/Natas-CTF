#!/bin/python3

import requests
import re
import html.parser

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
url = 'http://%s.natas.labs.overthewire.org' % (username)
data = {"secret" : "FOEIUWGHFEEUHOFUOIU" , "submit" : "submit" }
secret = "FOEIUWGHFEEUHOFUOIU"

#for getting a url without any session history
#response = requests.get(url, auth = (username,password))
#content = response.text

#for communicating with the website whilst maintaining session history
session = requests.Session()
response = session.post(url + '', data = data, auth = (username,password) )
content = html.unescape(response.text)


#for viewing the webpage
#print (content)
 

#for finding the password 
print (re.findall('The password for natas7 is (.*)',content)[0])
