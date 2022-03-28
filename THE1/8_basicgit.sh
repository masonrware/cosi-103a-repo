# Suppose you have cloned down the cs103a app from the github site.
# Do the following commands
# 1. fetch all of the branches from the site
# 2. list all of the branches
# 3. checkout the L25 branch (which contains two java script files)
# 4. checkout a new branch called myL25
# 5. modify the README.md to state that this is your version and save it with VScode
# 6. stage and commit your changes
# 7. switch back to the L25 branch

git fetch --all
git pull --all
git branch -a
git checkout L25    #! L25 does not exist on the app or class repo
git checkout -b myL25 <old-branch>  #? from old branch
#TODO
