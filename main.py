import github
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
g = github.Github(os.getenv("TOKEN"))

repo = g.get_user().get_repo("dev-tools-data")

file = repo.get_contents("./packages.json")
versionsFile = repo.get_contents("./versions.json")
pkgs = json.loads(file.decoded_content.decode("utf-8"))
versions = json.loads(versionsFile.decoded_content.decode("utf-8"))

for pkg in pkgs:
    x = requests.get(
        "https://api.github.com/repos/microsoft/winget-pkgs/contents/manifests/"
        + pkg["winget"][0].lower()
        + "/"
        + pkg["winget"].split(".")[0]
        + "/"
        + pkg["winget"].split(".")[1]
    )
    if x.status_code == 200:
        versions[pkg["name"]] = []
        vrs = json.loads(x.content.decode("utf-8"))
        for vr in vrs:
            if vr["name"].replace(".", "").isnumeric():
                versions[pkg["name"]].append(vr["name"])

for pkg in versions:
    versions[pkg] = sorted(versions[pkg], key=lambda x: [int(i) for i in x.split(".")])

repo.update_file(
    "./versions.json",
    "Update versions",
    json.dumps(versions, separators=(",", ":")),
    versionsFile.sha,
)
