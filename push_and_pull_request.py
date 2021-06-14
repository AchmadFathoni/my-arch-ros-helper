import os
from git import Repo, GitCommandError
from github import Github

g = Github(os.environ['GITHUB_TOKEN'])
user = g.get_user()
org = g.get_organization("ros-noetic-arch")

f = open("outdated_aur.txt","r")
path = "/home/toni/.cache/ros-aur-helper/packages/"
url = "git@github.com:AchmadFathoni/"
packages = [p for p in os.listdir(path) if os.path.isdir(path+p)]
packages.sort()
for package in packages:
# for package in f.readline().split():
    repo = Repo(path+package)
    try:
        remote = repo.remote("AchmadFathoni")
    except ValueError:
        repo.create_remote("AchmadFathoni", "git@github.com:AchmadFathoni/"+package+".git")
        remote = repo.remote("AchmadFathoni")
    finally:
        remote.push()
        # origin = org.get_repo(package)
        # pr = origin.create_pull("Upgrade",'','master','AchmadFathoni:master')
        print("Success ", package)
