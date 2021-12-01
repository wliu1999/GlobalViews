# GlobalViews Readme

## Heroku URL
[Heroku Link](https://global-views.herokuapp.com/)

## Initial Setup / Workflow order
Type in the terminal in order to finish initial setup

1. mkdir <your_dir_name> 
2. cd <your_dir_name>
3. git init
4. git remote add origin git@github.com:wliu1999/GlobalViews.git
5. git pull origin main

## Additional Setup Steps

1. Create an account on Google developer
2. Register your application with Google
3. Obtain an API key and a OAuth 2.0 Client ID. The OAuth ID should have application type Desktop app.
4. Create a .env folder to store hidden variables.
5. Download the OAuth 2.0 Client ID information as a json file, and input the API key into your .env file.
6. Create an account on Heroku and register your application there. 
7. Provision a postgresql database on heroku

After initial setup workflow order

1. git checkout -b <your_branch_name>
2. code and do things
3. git add --all
4. git commit -m 'comments'
5. git push origin <your_branch_name>
6. git checkout main
7. git merge <your_branch_name>
8. git branch -d <your_branch_name>
