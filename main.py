import github
import os
from dotenv import load_dotenv

load_dotenv()
g = github.Github(os.getenv("TOKEN"))

repo = g.get_user().get_repo("dev-tools-data")
file = repo.get_file_contents("/versions.json")

repo.update_file("/versions.json", "bot test commit", "hello world!", file.sha)
