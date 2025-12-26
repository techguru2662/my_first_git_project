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



'''


print("Hello GitHub from PyCharm!")



























































