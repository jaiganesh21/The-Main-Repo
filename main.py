from github import Github
import os

g = Github(os.environ["ACCESS_TOKEN"])

current_user = g.get_user()
print("Logged in as : ", current_user.login)

# Get the repository
repos = sorted(current_user.get_repos(), key=lambda x: x.created_at, reverse=True)


# store all the repository names in a list
all_repos = []
for repo in repos:
    if repo.owner.login == current_user.login:
        all_repos.append(repo.name)

# save the list to a file
with open("all_repo.txt", "w") as f:
    f.write(",".join(all_repos))
    
print("Successfull!!")
