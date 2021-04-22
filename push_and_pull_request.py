import os
from git import Repo, GitCommandError
from github import Github

g = Github(os.environ['GITHUB_TOKEN'])
user = g.get_user()
org = g.get_organization("ros-noetic-arch")

f = open("outdated_aur.txt","r")
path = "/home/toni/.cache/ros-aur-helper/packages/"
url = "git@github.com:AchmadFathoni/"
for line in f.readlines():
    package = line.split()[1][:-1]
    repo = Repo(path+package)
    remote = repo.remote("AchmadFathoni")
    remote.push()
    origin = org.get_repo(package)
    pr = origin.create_pull("Upgrade",'','master','AchmadFathoni:master')
    print("Success ", package)
    exit