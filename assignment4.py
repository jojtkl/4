# Python - Functions
# Python-Functions What does the len() function do in Python?
#len() function determines the number of items in an object. it is used in all types of datatypes.
# in strings len('Hallo') gives the values 5 ie number of character in the object which is string data types.
# in dictionary, it gives number of key value pairs.
# in list,tuple,list,set it gives number of elements.
# print(len('Hallo'))
# print(len([1,2,3,'tz',55]))
# print(len({'a':2,'b':5}))

# Write a code example using len() to find the length of a list.
# l1=[1,2,3,4,5]
# print(type(l1))
# print(len(l1))
# Write a Python function greet(name) that takes a person('s name as input and prints "Hello, [name]!". '
# name=str(input('Enter the name :'))
# def greet(name):
#     print(f'Hello,{name}!')
# greet(name)
# # Write a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value without using the built-in max() function.
#Use a loop to iterate through the list and compare values

# no=[22,33,44,55,66]
# def get_max(no):
#     max = no[0]
#     for i in no:
#         if i > max:
#             max = i
#     return max
# print(get_max(no))




# Explain the difference between local and global variables in a Python function.

# Local variable

# local variables are assigned Inside a function
#value is only for the particular function or a function which is inside the function Limited to the function
#lifetime	Until the function finishes
#Modification	Cannot affect the entire pgm,modification can be done using a 'global' functions.
# when the data is needed for only for a short space and purpose during a  pgm

# Global variable

# it is assigned in outside any function
# it can be Accessed  across the entire program ,even function can access the value.
# this variable value doesn't change Until the program finishes
#when the value of the variable needs or doesn't change during the entire period of program.

# Write a program where a global variable and a local variable have the same name and show how Python differentiates between them.
#Example
# x = 0         # Global variable
# def increment():
#     global x  # Declare that we're using the global variable
#     x += 1    # Modify the global variable by using 'global in the above line '
#     b=12
#     print(b)  #local variable
# increment()
# print("After incrementing, counter:", x)


# Create a function calculate_area(length, width=5) that calculates the area of a rectangle. If only the length is provided, the function should assume the width is 5.
# Show how the function behaves when called with and without the width argument.
#By calling the input and default width area
#length=int(input('Enter the number:'))
#def calculate_area(length,width=5):
#    area=length*width
#    print(area)
#area1=calculate_area(length)
#print(area1)

#providing both values for length and width

#print('## providing both values for length and width ##')

#def calculate_area2(length,width=5):
#    area=length*width
#    print(area)
#area2=calculate_area2(10,8)
#print(area2)
