import pacman_helper
import os
from git.repo.base import Repo

pacman_db = pacman_helper.getLocal()
DIR = '/home/toni/Documents/source_linux/AUR/'
REPO = 'https://aur.archlinux.org/'
for name, version in pacman_db:
    if not os.path.isdir(DIR+name):
        Repo.clone_from(REPO+name+'.git', DIR+name)