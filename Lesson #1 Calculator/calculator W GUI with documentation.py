#-----------------------------------------------------------------------------
# Name:        Calculator (main.py)
# Purpose:     Generates a calculator with user input for use in the ICS3U course. This calculator is GUI integrated.
#
# Author:      
# Created:     5-May-2021
# Updated:     6-May-2021
#-----------------------------------------------------------------------------

# This line will run the basics.py file (my example).
# You can comment this out when starting your exercise.
# All of your assignments/exercises should be written in main.py - you won't have to worry about this.
#import basics

# Start writing your code here! (and make sure to modify the header above!)


#I am importing the tkinter library here which will allow me to create a GUI for my calculator
from tkinter import *
from tkinter import messagebox

#This is a popup messagebox which can be used for telling the user something about your program. There are two arguments given that are being placed in widget. The first argument passed is the messagebox title and the second argument will be the string that appears as an output in the messagebox
messagebox.showinfo("REMINDER", "This calculator expects the first number, an operation, second number, and then equal sign to output answer")
messagebox.showinfo("LAYOUT","If the layout does not show some buttons, you can adjust the size of the console to fit the entire calculator, developer has to work on making it more responsive haha!")

#root initializes the widget that we are going to be calling for all purposes, and Tk() is used to initialize the interpreter that Replit server is going to be using to understand the Tkinter library
root = Tk()
#.title function is used to pass a string for the title of the calcualtor
root.title("Calculator")

#e variable is initializing the entry field for the calculator and there are three arguments being called. The first argument being called is the idenfication of the entry field, second argument being called is width of entry field and final entry field being called is the depth perception effect that the entry field has and its value 
e = Entry(root,width=55, borderwidth=5)
#e variable is called again with a .grid function to initialize the boundaries of the entry field
e.grid(row=1,column=1,columnspan=7, padx=10,pady=10)

#This function is used to get a number into the entry field after it has been clicked on the calculator. The parameter being passed is "number". When a number is clicked, the "current" variable will store the integer value obtained from the .get function, this integer value is taken from entry field. The delete function takes two parameters, it takes the initial index value which in python, starts a "0" to represent the first number, and the second parameter being passed is the "END" value which is the value that is at the end of the entry field in our case. In this case, our 0 index will tell our delete function that we want to start relative to our first number entered. The END parameter will tell our delete function in this instance to delete the string value in the entry field altogether as we do not want the numbers just yet. The e.insert function will now take three parameters. The first parameter is 0 which initializes the index position. The second parameter is our number output in this case, str(current) will take the stored interger value in the current variable and paste it as a string in the entry field, this stored value is the integer which is on the display screen right now and not what is pressed. The str(number) allows us to define the integer value of the button we pressed and the string value of the number being pressed is pasted onto the entry field. This allows us to make numbers larger than 1 digit.
def button_click(number):
  current = e.get()
  e.delete(0,END)
  e.insert(0,str(current) + str(number))

#This function is used to delete all variables from the start of the entry field to the end, essentially erasing all previous strings and integer values.
def button_clear():
  e.delete(0,END)

#this is the function which adds number together when the "+"" sign is pressed. The first number entered into the entry field will get stored into the first_number varibale. We have initialized f_num and math as global variables so they can be called outside this function as well, we will talk about this later on. The math variable in this scenario since it is an add function, it will have a string value of "addition". The global math variable can be used by the equal sign to identify what type of operation is taking place. The global variable f_num will have an integer value of the first_number variable which has been taken from the entry field earlier on in the function. The e.delete will allow us to delete all string values from the entry field in order to input our next number.
def button_add():
  first_number = e.get()
  global f_num
  global math
  math ="addition"
  f_num = int(first_number)
  e.delete(0,END)

#This function is for subtraction and follows the exact same procedure as the addition function with the only difference being the string value of the global math variable being "subtraction".
def button_subtract():
  first_number = e.get()
  global f_num
  global math
  math ="subtraction"
  f_num = int(first_number)
  e.delete(0,END)

#This function is for multiplication and follows the exact same procedure as the addition function with the only difference being the string value of the global math variable being "multiplication".
def button_multiply():
  first_number = e.get()
  global f_num
  global math
  math ="multiplication"
  f_num = int(first_number)
  e.delete(0,END)

#This function is for division and follows the exact same procedure as the addition function with the only difference being the string value of the global math variable being "division".
def button_divide():
  first_number = e.get()
  global f_num
  global math
  math ="division"
  f_num = int(first_number)
  e.delete(0,END)

#This function is for exponents and follows the exact same procedure as the addition function with the only difference being the string value of the global math variable being "exponent".
def button_exponent():
  first_number = e.get()
  global f_num
  global math
  math ="exponent"
  f_num = int(first_number)
  e.delete(0,END)

#This function is for the equal sign. In this function, once the equal sign has been pressed, it will take the current string value on the screen which is the second number and store it inside a second_number variable, then the e.delete function will delete all values from index 0 to the end of the entry field. Next, the if functions are going to refference the global math variable to determine, at which instance, which operation sign is pressed. Each operation button was assigned a math string value pertaining to the operation name, and these if statements will follow the operation rules of those buttons based on what is called. The e.insert is used to start the entry field output at index 0 and the second portion of this code uses the first number which has been saved as an integer value, and then, it adds this first number to the converted from string to integer value of the second number, this value is recieved from the second_number variable.
def button_equal():
  second_number = e.get()
  e.delete(0,END)
  if math == "addition":
    e.insert(0,f_num + int(second_number))
  elif math == "subtraction":
    e.insert(0,f_num - int(second_number))
  elif math == "multiplication":
    e.insert(0,f_num * int(second_number))
  elif math == "division":
    e.insert(0,f_num/int(second_number))
  elif math == "exponent":
    e.insert(0,f_num**int(second_number))
 



#All of these buttons pertain to the number they are labelled as from 0-9. They are stored inside variable and this is how they work. The "Button" part of the code initializes a button, the first parameter inside it is the source tkinter component this button is going to be on, in our case it is called root. Next parameter is a text string value which will put text on the button. Next two parameters deal with the x and y dimensions of the actual button. Finally, the last parameter is used to initialize a command which makes the button responsive. The "lambda" function allows us to recieve data values within a function when a button is pressed. Basically, when I press one, the lambda value is what allows us to store the value inside a variable which can be then used in a function as a parameter or an integer value.
button_1 = Button(root,text="1", padx=100, pady=20, command=lambda:button_click(1))
button_2 = Button(root,text="2", padx=100, pady=20, command=lambda:button_click(2))
button_3 = Button(root,text="3", padx=100, pady=20, command=lambda:button_click(3))
button_4 = Button(root,text="4", padx=100, pady=20, command=lambda:button_click(4))
button_5 = Button(root,text="5", padx=100, pady=20, command=lambda:button_click(5))
button_6 = Button(root,text="6", padx=100, pady=20, command=lambda:button_click(6))
button_7 = Button(root,text="7", padx=100, pady=20, command=lambda:button_click(7))
button_8 = Button(root,text="8", padx=100, pady=20, command=lambda:button_click(8))
button_9 = Button(root,text="9", padx=100, pady=20, command=lambda:button_click(9))
button_0 = Button(root,text="0", padx=100, pady=20, command=lambda:button_click(0))

#This code follows the same rules as above in terms of parameters except we do not need to use lambda for these functions as the operations do not have an assigned integer value, therefore, the function which addresses these buttons can take care of any output these buttons are suppose to produce.
button_equal = Button(root,text="=",padx=100,pady=20,command=button_equal)
button_clear = Button(root,text="clear", padx=87, pady=20, command=button_clear)
button_add= Button(root,text="+(Add)",padx=80,pady=20,command=button_add)
button_subtract = Button(root,text="-(Subtract)",padx=70,pady=20,command=button_subtract)
button_multiply= Button(root,text="*(Multiply)",padx=67,pady=20,command=button_multiply)
button_divide= Button(root,text="/(Divide)",padx=75,pady=20,command=button_divide)
button_exponent=Button(root,text="Exponent", padx=75,pady=20,command=button_exponent)


#The .grid functions are used to initialize the positioning of buttons on the grid. This grid was initiazlized earlier in the code when the root widget was setup. The grid starts with row = 1, column = 1, and this is located at the top most left of the buttons. This grid does not interfere with the entry field

button_1.grid(row=2,column=1)
button_2.grid(row=2,column=2)
button_3.grid(row=2,column=3)

button_4.grid(row=3,column=1)
button_5.grid(row=3,column=2)
button_6.grid(row=3,column=3)

button_7.grid(row=4,column=1)
button_8.grid(row=4,column=2)
button_9.grid(row=4,column=3)

button_0.grid(row=5,column=1)
button_equal.grid(row=7,column=3)
button_clear.grid(row=7,column=2)
button_add.grid(row=5,column=2)

button_subtract.grid(row=5,column=3)
button_multiply.grid(row=6,column=2)
button_divide.grid(row=6,column=1)
button_exponent.grid(row=6,column=3)



#-----------------------------------------------------------------------------
# Name:        Calculator (main.py)
# Purpose:     Generates a calculator with user input for use in the ICS3U course. This calculator is in the console-only
#
# Author:      
# Created:     5-May-2021
# Updated:     6-May-2021
#-----------------------------------------------------------------------------


#Operation variable stores an operation value entered by the user. All options are displayed.
operation = str(input("What is the operation you would like to do, example:\n + (Addition)\n - (Subtraction)\n * (Multiplication)\n / (Division)\n ** (Exponent)\n "))

# number_one variable asks user for their first number and converts the string value into an integer value
x = int(input("What is your first number: "))
# number_two variable asks user for their second number and converts the string value into an integer value
y = int(input("What is your second number: "))


#These if-statements are used to take the first and second number and perform and operation on them based on which operation was picked by the user. This data is given by the operation variable which stores the type of operation. Finally, the output to the operation is printed and sent to the console
if operation == "+":
 print("Your number is: " + str(x+y))

elif operation == "*":
  print("Your number is: " + str(x*y))

elif operation == "/":
  print("Your number is: " + str(x/y))

elif operation == "-":
  print("Your number is: " + str(x-y))

elif operation == "**":
  print("Your number is: " + str(x**y))

