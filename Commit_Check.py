import requests
import json

# Replace with your GitHub repository details
REPO_OWNER = "kdbhai"
REPO_NAME = "CI-CD_Pipeline_Assigment"

# Replace with your GitHub personal access token
GITHUB_TOKEN = "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"

def get_commits():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def check_for_new_commits(commits):
    latest_commit = commits[0]
    latest_commit_sha = latest_commit["sha"]
    # Compare with the previous latest commit SHA (stored in a file or database)
    try:
        with open("latest_commit_sha.txt", "r") as f:
            previous_latest_commit_sha = f.read()
        if latest_commit_sha != previous_latest_commit_sha:
            print("New commits found!")
            print(json.dumps(latest_commit, indent=4))
            with open("latest_commit_sha.txt", "w") as f:
                f.write(latest_commit_sha)
        else:
            print("No new commits found.")
    except FileNotFoundError:
        print("First run, saving latest commit SHA...")
        with open("latest_commit_sha.txt", "w") as f:
            f.write(latest_commit_sha)

if __name__ == "__main__":
    commits = get_commits()
    check_for_new_commits(commits)