حتماً! در ادامه نسخه‌ی **انگلیسی** فایل `README.md` برای اسکریپت GitLab issue creator:

---

````markdown
# GitLab Issue Creator with Table and Comments

This script uses the GitLab API to create a new issue in a specified GitLab project. It adds a formatted Markdown table as the issue description and appends multiple predefined comments.

---

## 📌 Features

- Creates a new **issue** in a GitLab project
- Adds a **Markdown table** to the issue description
- Appends **three predefined comments** to the issue
- Accepts the issue title as a command-line argument

---

## ⚙️ Requirements

- Python 3
- Python dependencies (install via pip):

```bash
pip install requests
````

* A GitLab **Personal Access Token** with `api` or `write_repository` scope

---

## 🔧 Configuration

Before running the script, edit the following variables in the Python file:

```python
ACCESS_TOKEN = "your_gitlab_access_token"
PROJECT_ID = "your_project_id"
```

To find your `PROJECT_ID`:

1. Open your project in GitLab
2. Go to `Settings > General`
3. Look for the **Project ID** section

---

## 🚀 Usage

```bash
python create_issue.py --title "Your issue title"
```

### Example:

```bash
python create_issue.py --title "Compare behavior between Zharf and Cisco"
```

---

## 🧾 What It Does

* Sends a POST request to create an issue in GitLab
* Adds a Markdown-formatted table in the description
* Posts three comments with predefined content
* Prints the created issue's URL and status to the console

---

## ✅ Sample Output

```
Creating issue: Compare behavior between Zharf and Cisco
Issue created successfully: #23
Issue URL: https://git.zharfpouyan.net/l3-switch/l3-switch/-/issues/23
Comment 1 added successfully.
Comment 2 added successfully.
Comment 3 added successfully.
Done.
```

---

## 🔒 Security Notice

Make sure not to share or commit your personal access token to public repositories.

---

