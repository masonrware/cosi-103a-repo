# Write the egrep command to recognize a localhost mongodb URL which has the form
# "mongodb://USER:PASSWORD@localhost:27017"
# where 
# * the USER:PASSWORD@ is optional
# * the USER is 3 or more lowercase letters
# * the PASSWORD is 8 or more characters
# * it must be contained with a quotes

# Create a file consisting of 6 or more lines of which three match the pattern and three almost match (but don't quite).
# Cut/paste your egrep command and the test files with 6+ lines.

# Also, create a short Zoom movie with a screen recording of you running egrep and egrep -v on your file
# and explaining how your regular expression works.



egrep '\"mongodb://[a-z]{3,}:.{8,}@localhost:27017\"' 6_sample_data.txt
#test file is located at ./6_sample_data.txt

#zoom link: