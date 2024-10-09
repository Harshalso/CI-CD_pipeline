import requests
import json

GITHUB_REPO = "https://api.github.com/repos/Harshalso/CI-CD_pipeline/commits"
LAST_COMMIT_FILE = "/home/ubuntu/last_commit.txt"

def get_latest_commit():
    response = requests.get(GITHUB_REPO)
    commits = response.json()
    return commits[0]['sha']

def read_last_commit():
    try:
        with open(LAST_COMMIT_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def write_last_commit(sha):
    with open(LAST_COMMIT_FILE, 'w') as f:
        f.write(sha)

def main():
    latest_commit = get_latest_commit()
    last_commit = read_last_commit()

    if latest_commit != last_commit:
        print("New commit detected!")
        write_last_commit(latest_commit)
        return True
    else:
        print("No new commits.")
        return False

if __name__ == "__main__":
    if main():
        # Trigger deployment script if new commit is found
        import subprocess
        subprocess.call(["/home/ubuntu/deploy.sh"])
