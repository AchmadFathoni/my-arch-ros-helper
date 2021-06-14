import subprocess
FILE = open("outdated_aur.txt","r")
PATH = "/home/toni/.cache/ros-aur-helper/packages/"
for package in FILE.readline().split():
    process = subprocess.Popen(
        ['makepkg', '-fiC'],
        cwd=PATH+package,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout, stderr)
