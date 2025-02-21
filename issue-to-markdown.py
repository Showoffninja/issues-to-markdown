import requests
import os

GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "bidma-nn"
REPO_NAME = "GDAI-Architecture"
OUTPUT_DIR = "issues"


def fetch_issues(repo_owner, repo_name, strheaders):
    print(f"Fetching issues from {repo_owner}/{repo_name}")
    print(f"Output directory: {strheaders}")
    url = f"{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}/issues?filter=all"
    response = requests.get(url, headers=strheaders, verify=False)
    response.raise_for_status()
    return response.json()


def write_issue_to_markdown(issue, output_dir):
    issue_number = issue["number"]
    issue_title = issue["title"]
    issue_body = issue["body"]
    filename = f"{output_dir}/issue_{issue_number}.md"

    with open(filename, "w") as file:
        file.write(f"# {issue_title}\n\n")
        file.write(issue_body)


def main(strheaders):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    issues = fetch_issues(REPO_OWNER, REPO_NAME, strheaders)
    for issue in issues:
        write_issue_to_markdown(issue, OUTPUT_DIR)


if __name__ == "__main__":
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    if not GITHUB_TOKEN:
        raise EnvironmentError("GITHUB_TOKEN environment variable is not set")

    strheaders = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }

    main(strheaders)
