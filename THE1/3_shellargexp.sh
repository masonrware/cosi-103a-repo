# Write the bash code to do the following
# 1) ssh into tiara
# 2) create a folder called args_test
# 3) cd into that folder
# 4) create 100 folders person00 to person99
# 5) inside each of those create files hw_A ... hw_E
# 6) use du -a to list all files and folders within the args_test folder
# 7) cd to your home folder
# 8) delete the args_test folder and everything inside it
# 9) exit tiara



ssh masonware@diadem.cs.brandeis.edu
mkdir args_test
cd args_test
mkdir person{00..99}
touch exam{00..99}/hw_{A..E}    #! ?

du -a       #! ?
cd ..
rm -r person{00..99}
exit