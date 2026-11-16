# Git and GitHub CLI Commands Used

These are all the commands we used to build and manage this project, in order.

## 1. Setup

| Command | What it does |
|---------|--------------|
| `git --version` | Checks that Git is installed |
| `git config --global user.name` | Shows / sets the name saved with every commit |
| `git config --global user.email` | Shows / sets the email saved with every commit |
| `gh auth status` | Checks that GitHub CLI is logged in to our GitHub account |

## 2. Start the repository

| Command | What it does |
|---------|--------------|
| `git init` | Creates a new empty Git repository in the folder |
| `git status` | Shows which files are new, changed or staged |
| `git add README.md .gitignore` | Moves files to the staging area |
| `git commit -m "Initial commit: add README and .gitignore"` | Saves a snapshot of the staged files |
| `git log --oneline` | Shows the commit history, one line per commit |

## 3. Connect to GitHub

| Command | What it does |
|---------|--------------|
| `gh repo create phishing-url-detector --public` | Creates a new public repository on GitHub |
| `git remote add origin https://github.com/vansh-mahajan1/phishing-url-detector.git` | Links the local repo to the GitHub repo |
| `git remote -v` | Shows the linked remote URLs |
| `git branch -M main` | Names the main branch `main` |
| `git push -u origin main` | Uploads `main` to GitHub and sets it as the default upstream |

## 4. Feature branch: URL checker

| Command | What it does |
|---------|--------------|
| `git branch feature/url-checker` | Creates a new branch |
| `git checkout feature/url-checker` | Switches to that branch |
| `git branch` | Lists all branches (`*` = current branch) |
| `git add detector.py` | Stages the detection logic |
| `git commit -m "Add rule-based URL checking logic"` | Commits it |
| `git diff` | Shows exactly what changed before committing the bug fix |
| `git commit -m "Fix false positives for official sites like accounts.google.com"` | Commits the fix |
| `git add main.py sample_urls.txt` | Stages the command line app |
| `git commit -m "Add command line interface and sample URLs"` | Commits it |
| `git push -u origin feature/url-checker` | Uploads the branch to GitHub |
| `git checkout main` | Goes back to `main` |
| `git merge feature/url-checker` | Merges the feature into `main` |
| `git push origin main` | Uploads the updated `main` |

## 5. Feature branch: Web app

| Command | What it does |
|---------|--------------|
| `git checkout -b feature/web-app` | Creates **and** switches to a new branch in one step |
| `git add app.py templates/index.html requirements.txt` | Stages the web app files |
| `git commit -m "Add Flask web page for checking URLs"` | Commits them |
| `git push -u origin feature/web-app` | Uploads the branch |
| `git checkout main` | Goes back to `main` |
| `git pull origin main` | Downloads any new changes from GitHub before merging |
| `git merge feature/web-app` | Merges the web app into `main` |
| `git push origin main` | Uploads the updated `main` |

## 6. Tests, docs and release

| Command | What it does |
|---------|--------------|
| `git add test_detector.py` | Stages the unit tests |
| `git commit -m "Add unit tests for detector"` | Commits them |
| `git add README.md GIT_COMMANDS.md` | Stages the documentation |
| `git commit -m "Update README and add list of git commands"` | Commits it |
| `git push origin main` | Uploads to GitHub |
| `git tag -a v1.0 -m "Version 1.0"` | Marks this commit as release version 1.0 |
| `git push origin v1.0` | Uploads the tag to GitHub |
| `git log --oneline --graph --all` | Shows the full history as a graph with branches and merges |

## 7. Check on GitHub

| Command | What it does |
|---------|--------------|
| `gh repo view` | Shows the GitHub repository details in the terminal |
| `git clone https://github.com/vansh-mahajan1/phishing-url-detector.git` | Downloads a fresh copy to check everything was pushed |

## Summary

**Git:** `init`, `config`, `status`, `add`, `commit`, `log`, `diff`, `branch`, `checkout`, `merge`,
`remote`, `push`, `pull`, `tag`, `clone`

**GitHub CLI:** `gh auth status`, `gh repo create`, `gh repo view`
