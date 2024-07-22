x=10   #create a variable and assign an integer
y=3.24  #float value
x=67  #reassigning the value to a variable x
z=x+y
z1=x*y
z2=x**y
z3=x%y
z4=x/y
z5=x//y

print(z,z1,z2,z3,z4,z5)
# string basics
#indexing and slicing
string="python is a programming language"
string1="creative source"
string2=str(1.334)   #when it converts into int datatype to string
print(string[0])  #first character
print(string[-1])  #last character
print(string[1:7])  #slice from index 1 to 7
print(string[6:])
print(string[:8])
#string methods
print(string.upper())  #converts to uppercase
print(string.lower())  #converts to lowercase
print(string.strip())  #removing whitespace
print(string.replace("python","AI"))  #Replace substring
#concatenation of two strings
print(string+' '+string1)
# f string formatting
print(f"source:{string},destination:{string1}")
print(type(string2))

number=int(input("please enter an integer"))#In a Python file, use input() to ask the user to enter an integer that 10 will be added to.
print(number+10)                              #print() the sum of the integer they entered and 10.

abc=2.34                                         #Create a variable and assign it a float
print(type(abc))
print(str(abc)+"is a float")
print("hello,I'M madhu ,it's nice to meet you!")
""" Use print() and type() to print the data type of the variable in the output
Use str() on the variable from step 1 and concatenate it with the string " is a float." then use print() to display the result
 print() the string "Hello, I'm [name], it's nice to meet you!" including quotes (you will need to use the \' or \" escape sequence depending on whether you enclose your strings in single quotes or double quotes."""
print("*******\n *****\n  ***\n   *")         
def hello_world_printer():                         #defining a function with 0 parameter
    print("python")
hello_world_printer()
def name_printer(name):
    print(name)                                     ##defining a function with 0 parameter
name = input("Please enter your name.")
name_printer(name)
score=int(input("enter the marks"))
if(score>=90):
    print("A GRADE")
elif(score>=80):
    print("B GRADE")
elif(score>=70):
    print("C GRADEE")
elif(score>=60):
    print("D GRADE")
elif(score<=50):
    print("F GRADE")

print("This is a branch test")
