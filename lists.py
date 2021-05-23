#-----------------------------------------------------------------------------
# Name:        List (main.py)
# Purpose:     Create a list and modify it according to the instructions
#
# Author:      
# Created:     05-May-2021
# Updated:     05-May-2021
#-----------------------------------------------------------------------------

grocery_list = []
while True:
  grocery = (input())
  if grocery == '!':
    break
  if grocery not in grocery_list:
    grocery_list.append(grocery)

#Sorts the list 
grocery_list.sort()
print (grocery_list)
#print third item
print(grocery_list[2])
#print item from third from the end of the list
print(grocery_list[-3])
#print 4th item through 6th
part = (grocery_list[3:6])
print (part)
#print the part variable backwards
print(part[::-1])
#remove last item
del grocery_list[-1]

existing_item = input()
#Removes item entered if it already exists in the list
if existing_item in grocery_list:
  grocery_list.pop (grocery_list.index(existing_item))
print (grocery_list)


# DO NOT CHANGE THIS LIST
intList = [5,8,-10,3,18,22,1,71]

# If item in list is odd, multiply by 2
# Print list
newList=[]
for number in intList:
  final = number
  if number%2==1:
    final = number*2
  newList.append(final)
print(newList)
