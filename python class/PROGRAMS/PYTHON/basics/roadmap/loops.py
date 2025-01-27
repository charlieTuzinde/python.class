

# LOOPS


# Loops in Python are used to execute a block of code repeatedly until a specific condition is met. They are fundamental for iterating over sequences (like lists, tuples, dictionaries, sets, and strings) and for running blocks of code multiple times. 






# Types of Loops in Python




#1 for Loop:

# Syntax: The for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) with an iterator variable.


'''# for element in sequence:
    # code block to be executed'''
# Example:



fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry



#2 while Loop:

# Syntax: The while loop is used to execute a block of code as long as a condition is true.
# while condition:
    # code block to be executed
# Example:


count = 0
while count < 5:
    print(count)
    count += 1
    # count+=1 MEANS you increment the count value by one each time the loop is called
# Output:
# 0
# 1
# 2
# 3
# 4




# Loop Control Statements
# These statements can change the flow of a loop from its normal sequence.






# break Statement:

# Terminates the loop and resumes execution at the next statement.


for i in range(10):
    if i == 6:
        break
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4




# continue Statement:

# Skips the rest of the code inside the loop for the current iteration and jumps to the next iteration.


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output:
# 1
# 3
# 5
# 7
# 9
# else Clause:

# The else part is executed if the loop completes normally (without encountering a break statement).


for i in range(5):
    print(i)
else:
    print("Loop finished")
# Output:
# 0
# 1
# 2
# 3
# 4
# Loop finished
# Nested Loops
# Loops can be nested inside other loops.


for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
# Output:
# i = 0, j = 0
# i = 0, j = 1
# i = 1, j = 0
# i = 1, j = 1
# i = 2, j = 0
# i = 2, j = 1
# Practical Examples
# Sum of Numbers:


numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("Total:", total)
# Output:
# Total: 15




# Factorial Calculation:


num = 5
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print("Factorial:", factorial)
# Output:




# Factorial: 120
# Iterating Over Dictionary:

student = {"name": "Alice", "age": 24, "course": "Mathematics"}
for key, value in student.items():
    print(key, ":", value)
# Output:
# name : Alice
# age : 24
# course : Mathematics
# Loops are powerful constructs that provide a way to perform repetitive tasks efficiently. Mastering them opens up a lot of possibilities for automating tasks and working with large datasets in Python. 
