# 1. Write the code to run the following command in the cs103aExpressApp folder
# node app.js
# Show how to run it in the background but send the output and the errors to a file nodeout.txt
# and show how to bring it to the foreground and kill it

# 2. Suppose you have started a process (e.g. with the command "nodemon" or "node app.js")
# but you need to pause it so you can check on the "git status".  How would you pause it,
# give the git status command, and the resume its execution.



node app.js &> nodeout.txt &
use the jobs command to find its job number N, then give the command kill%N
or give the command kill %nodemon  if it is the only nodemon job running

use the jobs command to find its job number N, then give the command ^Z to pause it
git status
#TODO