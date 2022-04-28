# Write the bash code to do the following:
# 1. ssh into tiara.cs.brandeis.edu
# 2. change directory to the /usr/local folder
# 3. list all of the files and folders in that folder with the long listing
# 4. change directory back to your home directory
# 5. print your working directory
# 6. change directory to /tmp
# 7. list all of the files in /tmp
# 8. change directory to the parent directory of /tmp
# 9. list the files
# 10. exit tiara



ssh masonware@diadem.cs.brandeis.edu
cd /usr/local/
ls -la
cd ../..
pwd
cd /tmp
ls -la
cd ..
ls -la
exit