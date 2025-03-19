[If viewing this in Git, click the </> button above to see the below properly. The IDE messes up the embedding]
        
1. Open our project on the GitLab website > Use the drop down to move to the master branch > Click 'Code' on the right > Click 'Download source code: zip' [You could use cloning instead but downloading the zip is simpler]

2. Work on your code within this folder

3. Delete your .venv and _pycache_ folders from the AAT folder, and the _pycache_ folder in the main folder - so that they don't get added to git

4. Save a backup copy of your code in another folder, incase the merge goes wrong (it may also be a good idea to save a backup of the whole team’s code)

5. Make your local folder a repo
        Open Git Bash
        Navigate into the folder
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
                If 'Resolve conflicts' button appears:
                        Click it
                        Make sure 'Side-by-side' and 'Interactive mode' are selected
                        Review the differences, and click either ‘Use their code’ or ‘Use our code' (Remember there may have been changes to the code since you last downloaded it)
                        At the bottom, click 'Commit to source branch'
                If 'Resolve conflicts' button doesn't appear, and it's telling you to resolve the conflicts locally:
                        1. Go back to Git Bash [If you'd closed it, navigate into your folder again then use 'git switch your-branch-name' (e.g., git switch anya-branch) to move back into your branch]
                        2. Run
                                git fetch origin
                                git fetch
                                git rebase origin/master [If you the 'Could not apply'... message, just ignore it]
                        5. Open the folder in VS code
                        6. Look at the conflicting area/s of code. The affected files are marked with a dot or a '!'. The conflicting code is marked between <<<<< and >>>>>.
                        7. Delete the code that no longer applies
                        8. Delete the conflict markers (<<<, === and >>>)
                        9. Save the changes
                        10. In Git Bash, run:
                                git add .
                                git commit -m "Fix merge conflicts"
                                git rebase --continue [If it says "Deletion of directory '.git/rebase-merge' failed. Should I try again? (y/n)", say 'n']
                                git push origin your-branch-name --force-with-lease (e.g., git push origin anya-branch --force-with-lease)
                        11. You should now be able to merge on the GitLab website as normal (see Step 10-11)
        Wait until it says 'Ready to merge!'
        Click 'Merge' [Don't worry if this button doesn't appear automatically, just go back to the 'Merge requests' tab and open the merge request again]

12. To check this merge didn't affect the website's functionality, download the master branch's code (see Step 1) and check it works (see README.md for how to run our website)