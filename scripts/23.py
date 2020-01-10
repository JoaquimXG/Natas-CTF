#!/bin/python3

import requests
import re
import html.parser

username = 'natas23'
password = "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"
url = 'http://%s.natas.labs.overthewire.org?passwd=11iloveyou' % (username)
session = requests.Session()

response = session.get(url + '' ,auth = (username,password))
content = response.text
# print (content)
print (re.findall("Password: (.*)</pre>",content)[0])

#this one is weird
#the source code when viewed on the site is easy enough to read
#but because of the colour styling they have decided to use 
#it was a nightmare to parse in the terminal 
#after tidying it up the actual code just requires for a string
#to be set as the value of a variable "passwd" and passed 
#through a GET request
#the variable then must meet two conditions 
#be greater than 10 
#and contain "iloveyou"

#this can be achieved in php with "11iloveyou"
