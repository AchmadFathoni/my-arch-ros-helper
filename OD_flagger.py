import os
import time
from lxml import html
import requests

login = {}
login['user'] = 'fathoni.id@gmail.com'
login['passwd'] ='qtpy>=1.5.0'
login['referer'] = 'https://aur.archlinux.org/'

s = requests.Session()
r = s.post('https://aur.archlinux.org/login', data=login)

f = open("outdated_aur.txt","r")
PREFIX = 'https://aur.archlinux.org/pkgbase/'
for line in f.readlines():
    package = line.split()[1][:-1]
    new_version = line.split()[3].strip("()").split('-')[0]
    url = PREFIX+package+'/flag/'
    p = s.get(url)

    payload = {}
    tree = html.fromstring(p.content)
    payload['ID'] = tree.xpath('//input[@name="ID"]/@value')[0]
    payload['IDs['+payload['ID']+']'] = '1'
    payload['token'] = tree.xpath('//input[@name="token"]/@value')[0]
    payload['comments'] = new_version + ' released'
    payload['do_Flag'] = 'Flag'

    p = s.post(url, data=payload)
    print(package, " ", p.status_code)
    time.sleep(5)
