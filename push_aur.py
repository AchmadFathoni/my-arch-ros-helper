from git import Repo, Git
import os
FILE = open("outdated_aur.txt","r")
PATH = "/home/toni/.cache/ros-aur-helper/packages/"
PREFIX_URL = "ssh://aur@aur.archlinux.org/"

global_git = Git()
global_git.update_environment(**os.environ)
for line in FILE.readlines():
    package = line.split()[1][:-1]
    repo = Repo(PATH+package)
    origin = repo.remote()
    print(package,' ', origin.push('master'))
