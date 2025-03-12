[If viewing this in Git, click the </> button above to see the below properly. The IDE messes up the embedding]
        
1. Download the latest version of our project, either through Git Bash cloning or by downloading the zip from the GitLab website

2. Work on your code within this folder

3. Delete your .venv and _pycache_ folders, so that they don't get pushed to git

4. Save a backup copy of your code in another folder, incase the merge goes wrong (it may also be a good idea to save a backup of the whole team’s code)

5. Make your local folder a repo
        open Git Bash
        cd into the folder
        git init
        git add . [You can add specific files instead if you want, but this way is quicker. Don't worry - as long as you review the changes properly during Step 11, this method won't cause any issues]
        git commit -m “Describe what you’ve changed” (I use “”s because then you can include ‘s inside it)

6. Make a new branch
        git checkout -b new-branch-name (e.g., git checkout -b anya-branch)

7. Check your new branch was successfully added
        git branch

8. Link your local repo to the online repo
        git remote add origin https://git.cardiff.ac.uk/c21127629/team2cmt313_assessment2.git

9. Push your new code to this branch
        git push origin new-branch-name (e.g., git push origin anya-branch)

10. On the GitLab website, create a merge request…
        Use the drop down to look at your new branch
        Check your files were successfully added
        Click ‘Create merge request’
        Underneath 'New merge request' click 'Change branches'
        Set the source branch to the branch you just made, and the target branch to 'master'
        Click 'Compare branches and continue'
        Write something in the 'Title (required)' box (e.g., 'Anya merging to Master')
        Ignore all of the options and scroll to the bottom
        Click 'Create merge request'

11. On the GitLab website, check your merge wouldn’t damage the rest of the code…
        Open your merge request
        If it says 'Merge blocked':
                Click 'Resolve conflicts'
                Make sure 'Side-by-side' and 'Interactive mode' are selected
                Review the differences, and click either ‘Use their code’ or ‘Use our code’ (Remember there may have been changes to the code since you last downloaded it)
                At the bottom, click 'Commit to source branch'
        Wait until it says 'Ready to merge!'
        Click 'Merge'

12. If you want to check this didn't damage anything - download the team's code again and check it works