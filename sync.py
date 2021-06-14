import requests 
import json
from git import Repo
from github import Github

s = requests.Session()
r = s.get('https://aur.archlinux.org/rpc/?v=5&type=search&by=maintainer&arg=AchmadFathoni')
data = json.loads(r.text)['results']
path = '/home/toni/.cache/yay/'
for datum in data:
    if 'ros-noetic-' in datum['Name'] and int(datum['FirstSubmitted']) < 1609512240:
        package = datum['Name'] 
        repo = Repo(path+package)
        try:
            remote = repo.remote('grup')
        except:
            repo.create_remote('grup', 'git@github.com:ros-noetic-arch/'+package+'.git')
            remote = repo.remote('grup')
        finally:
            remote.push()
            print("Success ", package)
