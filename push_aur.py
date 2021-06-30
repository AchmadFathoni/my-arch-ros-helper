from git import Repo, Git
import sys
import os

PATH = "/home/toni/.cache/yay/"
PREFIX_URL = "ssh://aur@aur.archlinux.org/"

global_git = Git()
global_git.update_environment(**os.environ)
for package in sys.argv[1:]:
    repo = Repo(PATH+package)
    repo.delete_remote('origin')
    origin = repo.create_remote('origin', PREFIX_URL+package+".git")
    origin.push('master')
    print(package)
