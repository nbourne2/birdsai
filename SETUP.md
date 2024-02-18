# Setting up a new Python Project in Astrosat
​
## Steps:

​1. Create new working directory  
2. Initialise Git for version control  
3. Create an initial commit with basic `README.md` and `.gitignore`  
4. Checkout new working branch  
5. Create Python environment  
6. Get to work
​
### 0. If using this template repo:
From [github.com/astrosat](https://github.com/astrosat), create a new repository, and select the template `astrosat/data-team-template`. Enter a name and description, set it to _Private_, and off you go.

_If using the template, skip steps 1-3 below._

### 1. Create new working directory
​
Go to wherever you want to keep the project and:
```bash
# Make a directory with project name, using lowercase and '-' for spaces
mkdir project-name
​
# Change directory to project directory
cd project-name
```
​
### 2. Initialise Git for version control
​
If you don't already have Git installed, follow instructions for installation [here](https://git-scm.com/downloads).
​
Initialise Git:
```bash
git init
```
​
This will create a `.git` directory.
​
### 3. Create an initial commit with basic `README.md` and `.gitignore`
​
In the project route directory, create a `README.md` file formatted using [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), this can be updated later, but worthwhile putting a basic project description here just now.  

Creating a `.gitignore` file just now is useful as it will ensure files to do with your working environment, or large data files don't get committed, bloating the repo and potentially messing with other peoples systems. [This](https://github.com/github/gitignore) repo provides some useful examples that can act as a lazy starting point.  

Once these files are created, stage, and commit them:
```bash
# Stage all unstaged files
git add .
​
# OR be more specific
git add README.md .gitignore
​
# And commit them:
git commit -m "Initial commit with README and .gitignore"
```
​
### 4. Checkout new working branch
​
Before doing any coding, need to move away from the master to ensure code is reviewed and working properly before it ends up in master.  

Create and new branch and move to it:
```bash
# Branch name saying what it is (feature) and a short description relating to a Github issue if relevant
git checkout -b feature/ISSUE#-NAME-OF-FEATURE
```
​
### 5. Create Python environment 
​
Many options exist for creating a Python environment that can be replicated on other systems. [Pipenv](https://pipenv.readthedocs.io/en/latest/) is recommended here as it ensures explicit versions are maintained, development only packages can be added, and works consistently across platforms.  

If not already installed, head to [Pipenv](https://pipenv.readthedocs.io/en/latest/) and follow the instructions.  

Creating a Pipenv environment and associated files:
```bash
# Start a Pipenv shell, and new subshell with a python environment activated
pipenv shell
# This will create a Pipfile, and Pipfile.lock which should be committed
​
# To exit, CTRL-d or
exit
```
​
Install python packages:
```bash
# From in the Pipenv shell
# Code packages
pipenv install <package-name>
​
# Development packages such as formatters, linters, jupyter etc
pipenv install --dev <package-name>
```
​
Setting up an environment where Pipfiles exist:
```bash
# Install just main packages
pipenv install
​
# Install development and main packages
pipenv install --dev
​
pipenv shell
```
​
Running code in the pipenv environment:
```bash
# Either work in a new shell using the virtualenv:
pipenv shell
# OR run commands from the current shell with the following prefix:
pipenv run <command>
```

### 6. Get to work
​
Do what you need to do, then:
- Commit regularly  
- Create a PR 

#### Commit messages:
Follow the [Astrosat guidelines](https://github.com/astrosat/company-wiki/wiki/Commit-guidelines) for commit messages.
In particular use e.g. `IssueID #1` to link commits with the issue they are addressing. This makes the log clearer when multiple branches are merged. 

#### Environment file:
A `.env` may be useful for providing environment variables to the virtualenv along with ensuring secrets are not stored in Git. `.env.EXAMPLE` shows a sample file that can be extended as required. 

#### Data storage:
Store data in the shared drive. This should mounted on `data1` and `data2` at `/home/<user>/shareddata/`. 
To mount it on your own computer see these [instructions](https://github.com/astrosat/company-wiki/wiki/How-to-mount-the-shareddata-network-share). 
The directory structure for shared project data is `shareddata/projects/<project-name>/`. You can also create your personal user directory in `shareddata/users/`.  

Depending on where the code is located, data can also be stored with the repo in a `data/` subdirectory (which by default will not be synched to Github). Alternatively, a symbolic link can be added within `data/` redirecting to directories on `shareddata`. 

To avoid hard-coding the locations of data, it is a good idea to specify the data directory in the `.env` file as the environment variable `DATA_PATH`. This can then be read in Python:
```python
import os
datadir = os.environ("DATA_PATH")
```

#### Some useful Git commands:

Various cheat-sheets can be found online, for example [this](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/gittutorial.html). The following commands are particularly useful: 
```bash
# Managing commits and synching to Github
git pull
git add
git rm
git commit [-a]
git tag <version-name> <commit-name>
git push [-u origin <branch>]

# Updating a branch to include more recent changes to master (or other base branch)
git checkout <branch>
git pull
git rebase <master> # Be very careful with this!

# Temporarily save changes to work on a different branch and then retrieve your previous work later
git stash
git checkout <some-other-branch-to-work-on>
<do stuff>
git stash pop

# Inspecting changes and status
git status  # current branch and status
git diff  # unstaged changes
git diff --cached  # staged changes
git diff <commit1> <commit2>  # compare commits
git diff --stat  # one-line summary of lines changed in each file
git diff --name-status  # list of files modified, added or removed
git log [-N] [--all] [--decorate] [--oneline]  # log of [last N] commits on branch [all branches] [with tags] [only first line of each]
git branch  # list branches and highlight current branch
# The following command lists branches sorted by their last modified date, showing the latest commit of each
# This is a useful command to assign to an alias
git for-each-ref --sort=committerdate refs/heads/ --format='\''%(HEAD) %(color:green)%(committerdate:short) %(color:yellow)%(refname:short)%(color:reset) - %(color:red)%(objectname:short)%(color:reset) - %(contents:subject) - %(authorname) (%(color:green)%(committerdate:relative)%(color:reset))'\'
```
