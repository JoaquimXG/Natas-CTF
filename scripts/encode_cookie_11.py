#!/bin/python3

import base64
import json

defaultdata = { "showpassword" : "no", "bgcolor" : "#ffffff" }
cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=="
key = ""

cdecode = base64.b64decode(cookie).decode('utf-8')

dencode = json.dumps(defaultdata)

for i in range(0,len(cdecode)):
    temp = chr((ord(cdecode[i]) ^ ord(dencode[i])))
    ti = 2
    if temp not in key:
        key += temp
    else:
        break

def xor(string,key):
    outtext = ""
    for i in range(0,len(string)):
        outtext += chr(ord(string[i]) ^ ord(key[i%len(key)]))
    return outtext

fdata = {"showpassword":"yes","bgcolor":"#ffffff"} 

excookie = base64.b64encode(xor(json.dumps(fdata,separators = (',',':')),key).encode('utf-8')).decode('utf-8')
