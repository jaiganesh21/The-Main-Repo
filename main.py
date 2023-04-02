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

# Get the repository
repos = sorted(current_user.get_repos(), key=lambda x: x.created_at, reverse=True)


# store all the repository names in a list
all_repos = []
for repo in repos:
    if repo.owner.login == current_user.login:
        all_repos.append(repo.name)

contents = ",".join(all_repos)


main_repo = g.get_repo("jaiganesh21/The-Main-Repo")

branch = main_repo.get_branch(main_repo.default_branch)

try:
    file = main_repo.get_contents("all_repo.txt")
    main_repo.delete_file(file.path, "Removing file", file.sha, branch.name)
    print("File deleted successfully")
except:
    pass

# Create or update the file
main_repo.create_file("all_repo.txt", "Created DB", contents, branch=branch.name)
print("File created successfully")

