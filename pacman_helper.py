import subprocess

def getLocal():
    proc1 = subprocess.Popen(['pacman', '-Qm'], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(
        ['grep', 'ros-noetic'], stdin=proc1.stdout,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    proc1.stdout.close()
    out, err = proc2.communicate()
    pacman_db = []

    if err:
        print(err)
    else:
        for package in out.decode().split('\n')[:-1]:
            name, version = package.split()
            version = version.split('-')[0]
            pacman_db.append([name,version])

    return pacman_db
