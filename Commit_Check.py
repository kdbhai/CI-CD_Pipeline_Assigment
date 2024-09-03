import requests
import json
import os

# GitHub repository details
REPO_OWNER = "kdbahi"
REPO_NAME = "CI-CD_Pipeline_Assigment"

# GitHub personal access token
GITHUB_TOKEN = "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"

def get_commits():
    """Fetch latest commits from GitHub API"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return []
    return response.json()

def check_for_new_commits(commits):
    """Check for new commits and print details"""
    print("Commits:", commits)
    if not commits:
        print("No commits found.")
        return

    latest_commit = commits[0]
    latest_commit_sha = latest_commit["sha"]

    # Check if latest commit SHA is stored in file
    if os.path.exists("latest_commit_sha.txt"):
        with open("latest_commit_sha.txt", "r") as f:
            previous_latest_commit_sha = f.read()
        if latest_commit_sha != previous_latest_commit_sha:
            print("New commits found!")
            print(json.dumps(latest_commit, indent=4))
            with open("latest_commit_sha.txt", "w") as f:
                f.write(latest_commit_sha)
        else:
            print("No new commits found.")
    else:
        print("First run, saving latest commit SHA...")
        with open("latest_commit_sha.txt", "w") as f:
            f.write(latest_commit_sha)

if __name__ == "__main__":
    commits = get_commits()
    check_for_new_commits(commits)