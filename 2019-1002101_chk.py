#!/usr/bin/env python
import os, sys
import hashlib
import requests
import sys

var1 = sys.argv[1] #token
URL = 'http://hotsix.kro.kr/re_result.php'


def getHash(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

file = sys.argv[1]

if os.path.exists(file):
    fileHash = getHash(file)
    tar1 = '68b3f069b0d313789bc63483192bca6c'
    tar2 = fileHash

if tar1 == tar2:
    data = {'token': var1, 'CVE2019-1002101': 'ture'}
    res = requests.post(URL, data=data)
    print(res.text)
    print("true")
    sys.exit()
else:
    print("false")
    sys.exit()

