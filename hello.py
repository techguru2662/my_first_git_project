'''

In the terminal:
1. Clear previous terminal requests by hitting ctrl+L
2. Type 'git init' to start a new repository in GitHub, which will show
'Initialized empty Git repository in C:/Users/Poser/PycharmProjects/GitAndGitHubWorkflows/.git/'
3. To link PyCharm to a specific GitHub repository:
    a. Go to GitHub
    b. click <>Code (green button) on the top right of the screen and copy the HTTP link
        i. SSH is for more secure connections, and will not be used in this demonstration
    c. Back in the PyCharm terminal, type 'git remote add origin https://github.com/techguru2662/my_first_git_project.git'
        i. the link is from step b.
4. Create the Main Branch in the repository - GitHub uses Main as it's default branch.
    a. In the terminal, type: 'git branch -M main'
        i. The local branch is now called Main, matching the GitHub branch, which keeps both PyCharm and GitHub in sync
5. Prepare for the next commit
    a. Type in the terminal, 'git add .'
        i. the '.' means everything inside the current project folder
        ii. the 'warning' is okay, as it is only showing that Git is changing the line ending to match Windows formatting
6. Saving the files in Git
    a. Type in the terminal, 'git commit -m "First commit with project files"'
        i. "First commit with project files" is just a note to remember what the save is about
    b. Type in the terminal, 'git pull origin main --allow-unrelated-histories'
        i. This is done as we already have a README.md file in GitHub, but not locally
        ii. This pulls the changes into our local project
    c. A new page will open as Git combines the 2 histories; one from the local project, and the other from GitHub
        i. To get out of the terminal screen; press Esc key, then type 'wq!' - THIS DID NOT WORK FOR ME?????!!!!!!
7. Push step. Not complete until the push step is completed
    a. Type in the terminal, 'git push -u origin main'
    b. Shows that the project is merged and the branch 'main' set up to track 'origin/main', which means the local branch
    and GitHub branch are fully connected.
    c. the README.md file is now a part of our local project as well, which will push to GitHub keeping both sides in sync
8. Updating versions in Git
    a. Changed the message below:
        i. was: 'print("Hello GitHub from PyCharm!")'
        ii. now: 'print("Hello GitHub, this is an updated message!")
    b. Type in the terminal, 'git status' to see if Git noticed any changes in our project after we updated the print function
        i. The terminal shows that one file has been modified and the file is the hello.py file
    c. Type in the terminal, 'git add hello.py' so Git knows we want to save the change






'''


print("Hello from Developer Anders!")



























































