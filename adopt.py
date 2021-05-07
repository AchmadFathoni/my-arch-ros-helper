import requests
import time
from lxml import html

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
    url = PREFIX+package
    p = s.get(url)

    payload = {}
    tree = html.fromstring(p.content)
    payload['token'] = tree.xpath('//input[@name="token"]/@value')[0]
    payload['do_Adopt'] = "Adopt+Package"
    p = s.post(url+'/adopt/', data=payload)
    print(package, " ", p.status_code)
    time.sleep(2)
