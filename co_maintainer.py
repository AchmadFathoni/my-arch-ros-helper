import requests
import time
import json
from lxml import html

login = {}
login['user'] = 'fathoni.id@gmail.com'
login['passwd'] ='qtpy>=1.5.0'
login['referer'] = 'https://aur.archlinux.org/'

s = requests.Session()
r = s.post('https://aur.archlinux.org/login', data=login)
r = s.get('https://aur.archlinux.org/rpc/?v=5&type=search&by=maintainer&arg=AchmadFathoni')
data = json.loads(r.text)['results']
PREFIX = 'https://aur.archlinux.org/pkgbase/'

for datum in data:
    if 'ros-noetic-' in datum['Name'] and int(datum['FirstSubmitted']) < 1609512240:
        package = datum['Name'] 
        url = PREFIX+package
        p = s.get(url)

        payload = {}
        tree = html.fromstring(p.content)
        payload['token'] = tree.xpath('//input[@name="token"]/@value')[0]
        payload['users'] = "acxz"
        payload['do_EditComaintainers'] = "Save"
        p = s.post(url, data=payload)
        print(package, " ", p.status_code)
        time.sleep(2)
