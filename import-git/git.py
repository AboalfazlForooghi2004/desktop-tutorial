import argparse
import requests
import sys


ACCESS_TOKEN = ""
PROJECT_ID = "322" 


parser = argparse.ArgumentParser(description="Create a GitLab issue with table and comments")
parser.add_argument('--title', required=True, help='Issue title')

args = parser.parse_args()
issue_title = args.title


ISSUE_DESCRIPTION = """| ردیف  | باگ |    توضیحات   |  اولویت   |  وضعیت   |
| ------ | ------ |-------|-------- |--------|
|      1     |        |          |           |          |
|      2     |        |          |           |          |
|      3     |        |          |           |          |
|      4     |        |          |           |          |

/cc @nazari_s"""

COMMENTS = [
    "### لیست تفاوت های رفتاری ژرف و سیسکو",
    "### لیست تمامی تست هایی که برای سرویس انجام میشود",
    "### لیست تمامی ایشو های ثبت شده در پروژه product و l3-switch (تعیین وضعیت)"
]


GITLAB_API_URL = "https://git.zharfpouyan.net/api/v4"
headers = {
    "PRIVATE-TOKEN": ACCESS_TOKEN
}

# Create issue
print(f" Creating issue: {issue_title}")
create_issue_url = f"{GITLAB_API_URL}/projects/{PROJECT_ID}/issues"
issue_payload = {
    "title": issue_title,
    "description": ISSUE_DESCRIPTION
}

try:
    issue_response = requests.post(create_issue_url, headers=headers, json=issue_payload)
    issue_response.raise_for_status()
    issue = issue_response.json()
    issue_iid = issue["iid"]
    print(f" Issue created successfully: #{issue_iid}")
    print(f"Issue URL: https://git.zharfpouyan.net/l3-switch/l3-switch/-/issues/{issue_iid}")
except requests.exceptions.RequestException as e:
    print(f" ERROR: Failed to create issue → {e}")
    sys.exit(1)

# Add comments
for i, comment in enumerate(COMMENTS, start=1):
    note_url = f"{GITLAB_API_URL}/projects/{PROJECT_ID}/issues/{issue_iid}/notes"
    note_payload = {"body": comment}
    try:
        note_response = requests.post(note_url, headers=headers, json=note_payload)
        note_response.raise_for_status()
        print(f" Comment {i} added successfully.")
    except requests.exceptions.RequestException as e:
        print(f" WARNING: Failed to add comment {i} → {e}")

print(" Done.")