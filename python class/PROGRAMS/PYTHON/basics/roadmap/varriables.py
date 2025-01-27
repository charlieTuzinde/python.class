# Variables in Python are used to store data that can be used and manipulated throughout a program. They act as containers for values and provide a way to reference and manage data efficiently.

# ### Declaring Variables
# In Python, you don't need to declare a variable's type. You simply assign a value to a variable name using the assignment operator (`=`).
# Variables do not need to be declared with any particular type, and can even change type after they have been set.

# Examples of variable assignment
name = "Alice"           # String
age = 25                 # Integer
height = 5.7             # Float
is_student = True        # Boolean



# CASTING
# If you want to specify the data type of a variable, this can be done with casting.
# casting will by itself choose whether to give the output according to the datatpe you have specified
# Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


### Variable Naming Rules
# - Must start with a letter (a-z, A-Z) or an underscore (_).
# - Cannot start with a number.
# - Can only contain alphanumeric characters and underscores.
# - Case-sensitive (`name` and `Name` are different variables).
# - Should not be a Python keyword (e.g., `for`, `while`, `class`).



### Variable Types
# Variables in Python can store different types of data. Common types include:

# 1. **Integers**: Whole numbers, positive or negative.

count = 10
 
# 2. **Floats**: Decimal numbers.
   
temperature = 36.6


# 3. **Strings**: Sequences of characters, enclosed in single or double quotes.BOTH the quotes work in the same way and they give the same result.
   
greeting = "Hello, World!"
print(greeting)

# 4. **Booleans**: True or False values.

is_active = True
   

# 5. **Lists**: Ordered collections of items.
 
fruits = ["apple", "banana", "cherry"]
   

# 6. **Tuples**: Ordered, immutable collections of items.
   
point = (10, 20)
   

# 7. **Dictionaries**: Unordered collections of key-value pairs.
   
student = {"name": "Alice", "age": 25}
   

# 8. **Sets**: Unordered collections of unique items.


colors = {"red", "green", "blue"}
   

### Changing Variable Values
# Variables can be reassigned to new values at any time.

x = 10
print(x)  # Output: 10

x = 20
print(x)  # Output: 20


### Variable Scope
# The scope of a variable determines where it can be accessed within a program.

# - **Global Variables**: Declared outside of any function and can be accessed anywhere in the program.
# - **Local Variables**: Declared inside a function and can only be accessed within that function.


# Global variable
x = "global"

def my_function():
    # Local variable
    x = "local"
    print(x)

my_function()  # Output: local
print(x)       # Output: global



### Best Practices
# - Use meaningful variable names that describe the data they hold.
# - Follow naming conventions (e.g., snake_case for variables).
# MULTI-WORD NAMING CONVENTIONS
# Camel Case
# Each word, except the first, starts with a capital letter:
# myVariableName = "John"
# Pascal Case
# Each word starts with a capital letter:

# MyVariableName = "John"
# Snake Case
# Each word is separated by an underscore character:

# my_variable_name = "John"


# - Keep the scope of variables as limited as possible to reduce complexity.
# Variables are fundamental to programming in Python, allowing you to store, manage, and manipulate data efficiently. Understanding how to use them effectively is crucial for writing clear and maintainable code. 