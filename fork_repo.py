import os
from github import Github, GithubException

g = Github(os.environ['GITHUB_TOKEN'])
user = g.get_user()
org = g.get_organization("ros-noetic-arch")
for repo in org.get_repos():
    try:
        print("Forking ", repo.url)
        repo.get_contents("/")
        user.create_fork(repo)
    except GithubException as e:
        print(e.args[1]['message'])
