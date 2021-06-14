from git import Repo, Git
import os
FILE = open("outdated_aur.txt","r")
PATH = "/home/toni/.cache/ros-aur-helper/packages/"
PREFIX_URL = "ssh://aur@aur.archlinux.org/"

global_git = Git()
global_git.update_environment(**os.environ)
for package in FILE.readline().split():
    repo = Repo(PATH+package)
    repo.delete_remote('origin')
    origin = repo.create_remote('origin', PREFIX_URL+package+".git")
    origin.push('master')
    print(package)
