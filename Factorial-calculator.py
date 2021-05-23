#-----------------------------------------------------------------------------
# Name:        For and While Loops (main.py)
# Purpose:     Do factorial calculations
#
# Author:      Armaan Rasheed
# Created:     13-May-2021
# Updated:     13-May-2021
#-----------------------------------------------------------------------------

import loops

#TASK 1
#Input variable 
number = int(input())
#Initializing answer variable
ans = 1

#if function determines whether number is bigger than or equal to one
if number >= 1:
  #while the number is bigger than one, the following tasks will be executed
  while number > 1:
    ans = ans *number
    number = number-1
  print(ans)
  

#TASK 2
#Input variables
begin = int(input())
end = int(input())
total = 0

#Determines whether end is smaller than begin resulting in an error if true
if end < begin:
  print("Error.")

#Determines whether begin is smaller than end resulting in the for loop starting. The for loop uses begin and end as start and stop variables
if end > begin:
  for count in range(begin,end,1):
    total += begin
    begin = begin + 1
    final = total + begin
  print(final)
#if begin is greater than end, Error. prints
elif begin>end:
  print("Error.")
#if begin is equal to end, then begin is printed
elif begin==end:
  print(begin)
