
# Functions in Python are essential building blocks that allow you to encapsulate code for reuse, modularity, and clarity. They can perform a specific task and can be called whenever needed. 

# Defining a Function
# Use the def keyword to define a function, followed by the function name and parentheses ().


def greet():
    print("Hello, World!")
# Calling a Function
# Simply call the function by its name followed by parentheses.


greet()  # Output: Hello, World!



# Parameters and Arguments
# Functions can accept parameters to make them more flexible.


def greet(name):
    print(f"Hello, {name}!")
# the below line must be indented .. this is a rule in python that cannot be avoided cause the code will not run
greet("Alice")  # Output: Hello, Alice!
# Default Parameters
# You can define default values for parameters.


def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Output: Hello, Guest!
greet("Bob")   # Output: Hello, Bob!
# Return Values
# Functions can return values using the return statement.


def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8



# Variable Scope
# Variables defined inside a function are local to that function.


def my_function():
    local_variable = 10
    print(local_variable)

my_function()  # Output: 10
# print(local_variable)  # Error: NameError


# Lambda Functions

# Anonymous functions defined using the lambda keyword, typically for short, throwaway functions.


add = lambda x, y: x + y
print(add(2, 3))  # Output: 5





# Higher-Order Functions
# Functions that take other functions as arguments or return them.

def apply_func(func, value):
    return func(value)

double = lambda x: x * 2
print(apply_func(double, 5))  # Output: 10


# Decorators
# Functions that modify the behavior of other functions.


def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before the function.
# Hello!
# Something after the function.
# Recursive Functions
# Functions that call themselves.


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120




# Practical Examples
# Sum of a List:


def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4]))  # Output: 10


# Fibonacci Sequence:


def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
# Functions in Python help you write clean, reusable, and efficient code. By mastering functions, you gain the power to tackle complex problems with organized and modular solutions. 



# SOME RE USABLE CODE BLOCKS


### 1. Calculate the Factorial of a Number

def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

### 2. Check if a String is a Palindrome

def is_palindrome(s):
    """Check if the given string s is a palindrome."""
    return s == s[::-1]


### 3. Get the Fibonacci Sequence

def fibonacci(n):
    """Return a list of the first n Fibonacci numbers."""
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


### 4. Find the Largest Element in a List

def find_max(lst):
    """Return the largest element in a list."""
    if not lst:
        raise ValueError("The list is empty.")
    return max(lst)


### 5. Sort a List of Dictionaries by a Key

def sort_dicts_by_key(lst, key):
    """Sort a list of dictionaries by a specified key."""
    return sorted(lst, key=lambda x: x[key])


### 6. Calculate the Mean of a List of Numbers

def calculate_mean(numbers):
    """Return the mean of a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty.")
    return sum(numbers) / len(numbers)


### 7. Generate a Random Password

import random
import string

def generate_password(length=12):
    """Generate a random password of a given length."""
    if length < 4:
        raise ValueError("Password length should be at least 4.")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


### 8. Convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

### 9. Check if a Number is Prime

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

### 10. Read a File and Count Word Frequencies

from collections import Counter

def count_word_frequencies(file_path):
    """Count the frequency of words in a text file."""
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    return Counter(words)


# ### How to Use These Functions
# You can copy and paste these function definitions into your Python script or interactive environment. Here’s an example of how to use one of them:


# Example usage of the factorial function
try:
    print(factorial(5))  # Output: 120
except ValueError as e:
    print(e)




# MORE
# PYThon consists of different Modules , Libraries or pakages . They consists of alot of pr-defined  functions for different ttopics  or areas , such as mathem,atics,  plotting, handling database systems, etc.