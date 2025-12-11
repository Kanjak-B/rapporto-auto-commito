# Script to get day commits

from git import Repo
from datetime import datetime

repo_path = "/home/kanjak/Bureau/INT/Projects/rapporto-auto-commito"

repo = Repo(repo_path)
commits = list(repo.iter_commits('main'))

today = datetime.now().date()

print(f"Récupération des commits du : {today}")
print("-" * 50)

for commit in commits:
    if commit.committed_datetime.date() == today:
        print("Commit:", commit.hexsha)
        print("Auteur :", commit.author.name, f"<{commit.author.email}>")
        print("Date   :", commit.committed_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        print("Message:", commit.message.strip())
        print("-" * 50)
