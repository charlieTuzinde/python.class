# Conditionals in Python are a way to execute code based on certain conditions. The main conditional statements are `if`, `elif`, and `else`. Here’s a breakdown of how they work, along with examples.

### Basic Structure

# 1. **If Statement**: Checks a condition and executes a block of code if the condition is true.
# 2. **Elif Statement**: Stands for "else if." It checks another condition if the previous `if` was false.
# 3. **Else Statement**: Executes a block of code if none of the preceding conditions were true.

### Syntax


# if condition:
#     # code to execute if condition is true
# elif another_condition:
#     # code to execute if another_condition is true
# else:
#     # code to execute if all previous conditions are false


### Example 1: Basic If-Else


age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# **Output:**
# ```
# You are an adult.
# ```

### Example 2: If-Elif-Else


score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")
# 

# **Output:**
# ```
# Grade: B
# ```

### Example 3: Nested Conditionals

# You can nest conditionals within each other.


number = 7

if number > 0:
    print("Positive number")
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Non-positive number")


# **Output:**
# ```
# Positive number
# Odd number
# ```

### Example 4: Using Logical Operators

# You can combine conditions using logical operators (`and`, `or`, `not`).


x = 10
y = 20

if x > 5 and y > 15:
    print("Both conditions are true.")
else:
    print("One or both conditions are false.")


# **Output:**
# ```
# Both conditions are true.
# ```

### Example 5: Ternary Conditional Operator

# Python also supports a shorthand way to write conditionals, known as a ternary operator.


is_even = True
result = "Even" if is_even else "Odd"
print(result)

# **Output:**
# ```
# Even
# ```
# if is-even is initialiized to false then the outpuutt would be odd




### Example 6: Using Conditionals with Lists

# You can use conditionals to filter lists or check conditions on list elements.


numbers = [1, 2, 3, 4, 5]
evens = [num for num in numbers if num % 2 == 0]

print("Even numbers:", evens)

# **Output:**
# ```
# Even numbers: [2, 4]
# ```



### Example 7: Handling Exceptions with Conditionals

# You can also use conditionals in exception handling.


try:
    value = int(input("Enter a number: "))
    if value < 0:
        print("Negative number")
    else:
        print("Non-negative number")
except ValueError:
      # instead of simply throwing an error , it displays the message associated withj the error
    print("That's not a valid number.")


### Conclusion

# Conditionals in Python provide a powerful way to control the flow of your program based on conditions. By using `if`, `elif`, and `else`, along with logical operators and nesting, you can create complex decision-making structures to suit your needs.