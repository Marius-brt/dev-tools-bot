import github
import os
import json
from dotenv import load_dotenv

load_dotenv()
g = github.Github(os.getenv("TOKEN"))

repo = g.get_user().get_repo("dev-tools-data")

versions = repo.get_contents("./versions.json")
print(json.loads(file.decoded_content.decode("utf-8")))

""" repo.update_file(
    "./versions.json", "bot test commit", json.dumps(obj, indent=4), file.sha
) """
