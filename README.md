# Hello Friends this is a readme

## Initial Setup / Workflow order
Type in the terminal in order to finish initial setup

1. mkdir <your_dir_name> 
2. cd <your_dir_name>
3. git init
4. git remote add origin git@github.com:wliu1999/GlobalViews.git
5. git pull origin main

After initial setup workflow order

1. git checkout -b <your_branch_name>
2. code and do things
3. git add --all
4. git commit -m 'comments'
5. git push origin <your_branch_name>
6. git checkout main
7. git merge <your_branch_name>
8. git branch -d <your_branch_name>