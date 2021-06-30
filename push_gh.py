import os
import sys
from git import Repo

path = "/home/toni/.cache/yay/"
url = "git@github.com:ros-noetic-arch/"
for package in sys.argv[1:]:
    repo = Repo(path+package)
    try:
        remote = repo.remote("github")
    except ValueError:
        remote = repo.create_remote("github", url+package+".git")
    finally:
        remote.push()
        print("Success ", package)
