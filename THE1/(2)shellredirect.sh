# 1. Write the bash code to ssh into tiara.cs.brandeis.edu and then to count the number of files in /tmp.
# (Do this by using ls -l to print them out one per line and wc to count the lines)

# 2. Write the bash code to print out the 200 through 205th lines of /etc/passd 
# Assuming you are on tiara.cs.brandeis.edu you should get

# dang:x:3052:60:Dan Griffin,Grad  110,2744,,2:/home/g/grad/dang:/bin/tcsh
# qun:x:3053:60:Qun Ju,Grad  111,2719,,2:/home/g/grad/qun:/bin/tcsh
# paulb:x:3054:60:Paul Buitelaar,Grad  110,2712,,2:/home/g/grad/paulb:/bin/tcsh
# aeg:x:3055:60:Andrew Garland,Grad  110,2744,,2:/home/r/aeg:/bin/tcsh
# dabrams:x:3056:60:David Abrams,Grad  110,2745,5276846,2:/home/g/grad/dabrams:/bin/tc

ssh masonware@diadem.cs.brandeis.edu
cd /tmp
ls -l | wc

sed -n 201,205p passwd