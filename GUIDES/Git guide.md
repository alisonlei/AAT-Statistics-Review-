1. Download the latest version of our project, either through Git Bash cloning or by downloading the zip

2. Work on your code within this folder

3. Delete your .venv and _pycache_ folders, so that they don't get pushed to git

4. Save a backup copy of your code in another folder, incase the merge goes wrong (it may also be a good idea to save a backup of the whole team’s code)

5. Make your local folder a repo
        open Git Bash
        cd into the folder
        git init
        git add .
        git commit - “Describe what you’ve changed” (I use “”s because then you can include ‘s inside it)

6. Make a new branch
        git checkout -b new-branch-name (e.g., git checkout -b anya-branch)

7. Check your new branch was successfully added
        git branch

8. Push your new code to this branch
        git push origin new-branch-name (e.g., git push origin anya-branch)

9. On the GitLab website, create a merge request…
        Use the drop down to look at your new branch
        Check your files were successfully added
        Click ‘Create merge request’
        Make sure it says ‘into master’

10. On the GitLab website, check your merge wouldn’t damage the rest of the code…
		[I can’t remember exactly what it said but something like…]
        Click ‘Fix here’
        View it in ‘Interactive mode’
        View it in ‘Side by Side’ mode
        Review the differences, and click either ‘Use their code’ or ‘Use our code’
        Click ‘Merge Pull Request’
        Click ‘Confirm’

11. If you want to check this didn't damage anything - download the team's code again and check it works