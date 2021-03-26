import requests
import gzip
import io

from debian_parser import PackagesParser #https://aur.archlinux.org/packages/python-debian-parser/
from pkg_resources import packaging

import pacman_helper


#Download data from ROS repository
url = 'http://repositories.ros.org/ubuntu/main/dists/focal/main/binary-amd64/Packages.gz'
file_gz = io.BytesIO(requests.get(url).content)
data = gzip.GzipFile(fileobj=file_gz).read().decode()

#Parse data from ROS repository
parser = PackagesParser(data)
raw = parser.parse()
ros_db = []
for package in raw:
    name = package[0].get('value')
    if 'dbgsym' not in name and 'noetic' in name:
        for field in package:
            if field.get('tag') == 'Version':
                version = field.get('value').split('-')[0]
                ros_db.append([name,version])
                break

#Get ros packages data from local pacman
pacman_db = pacman_helper.getLocal()
    
#Compare both data
last_i=0
for name,current_version in pacman_db:
    for i in range(last_i, len(ros_db)):
        if ros_db[i][0] == name:
            current_version = packaging.version.parse(current_version)
            new_version = packaging.version.parse(ros_db[i][1])
            if(current_version < new_version):
                print(name,end=' ')
            last_i = i
            break
            