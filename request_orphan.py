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
COMMENTS = """
It's been more than 2 months since the maintainer is too occupied to maintain any ros-noetic-* packages and those packages are out-of-date[3]

[3]https://github.com/ros-noetic-arch/ros-noetic-desktop-full/issues/20
"""
for line in f.readlines():
    package = line.split()[1][:-1]
    p = s.get(PREFIX+package+'/request/')

    payload = {}
    tree = html.fromstring(p.content)
    payload['ID'] = tree.xpath('//input[@name="ID"]/@value')[0]
    payload['IDs['+payload['ID']+']'] = '1'
    payload['token'] = tree.xpath('//input[@name="token"]/@value')[0]
    payload['comments'] = COMMENTS
    payload['type'] = 'orphan'
    payload['merge_into'] = ''
    payload['do_FileRequest'] = "Submit Request"
    p = s.post(PREFIX, data=payload)
    print(package, " ", p.status_code)
    time.sleep(5)
