# Description

The user has a file that is made up of short (less than 1000 character) strings,
each on a different line (assume any common character or character combination
that means a newline to someone might be used interchangeably in this file).
Most of these strings will be preceded by numbers, i.e. “2 Steaks”, “10 Chicken
Wings”, “343GuiltySparks”. Accept the file from the user and return them a file
with the same items sorted first by the numeric value of any leading number (2
< 10 < 343) and then alphabetically for the rest of the string.

# Usage

Replace `input.txt` with your desired input file.

Build and run:

`docker build -t mysidewalk-sort .`
`docker run -ti mysidewalk-sort`
