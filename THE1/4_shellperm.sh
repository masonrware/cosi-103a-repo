# 0. Create a folder exam7_test and add 10 files test00.txt  through test10.txt

# 1. Write the shell commands which make everything in exam7_test readable and executable, but not writable by you.
#    Also remove all permissions for everyone else, in your group or otherwise, except for the file test00.txt which 
#    should be readable and executable but not writable by everyone in your group or not.  Run ls -l to show the files have the right permissions.

# 2. Sometimes you need to delete a folder but some of its subfiles and folders have permissions that don't allow you to remove them. 
#    Write the bash shell commands to change the permissions of every file and folder, and subfolder, etc in exam7_test to allow you 
#    to write it, and then give the command to delete the folder and all files within it.



mkdir exam7_test
touch exam7_test/test{00..10}.txt    #! ?

#you can r and x but not w, group can do everything, everyone can do everything

chmod -R 500 exam7_test
chmod 555 exam7_test/test00.txt
ls -l

#TODO
