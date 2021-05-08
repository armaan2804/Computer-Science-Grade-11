#-----------------------------------------------------------------------------
# Name:        Conditional Statements (main.py)
# Purpose:     Using it to run test cases for conditional statements
#
# Author:      Armaan Rasheed
# Created:     7-May-2021
# Updated:     7-May-2021
#-----------------------------------------------------------------------------

# Comment out the line below when you're done with the lesson code.
import conditionals

# You will check the 'grade' variable using if/elif/else statements.
# Your output must EXACTLY MATCH what is requested in TASK.md

#mark variable created to store the grade of student
mark = int(input())

#conditional statement is true if mark is above or equal to 80 and below or equal to 100, exceeding expectations will print to console
if mark >= 80 and 100 >= mark:
  print("Exceeding Expectations.")
#conditional statement is true if mark is between or equal to 70 and 79, meeting expectations will be printed to console
elif mark >= 70 and 79>=mark:
  print("Meeting Expectations.")
#conditional statement is true if mark is between or equal to 50 and 69, needs improvement will be printed to console
elif mark >=50 and 69>=mark:
  print("Needs Improvement.")
#conditional statement is true if mark is between or equal to 0 and 49, not passing will be printed to console
elif 49 >= mark and mark >=0:
  print("Not Passing.")
#conditional statement is true if mark is an invalid input, usually a negative value or above 100 or letters/symbols
else:
  print("Invalid Grade.")
