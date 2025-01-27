# A common programming task is to find the largest or smallest value in a series of values. Here is
# an example where we ask the user to enter ten positive numbers and then we print the largest one.
largest = eval (input("Enter a positive number:"))
for i in range(9):
    num = eval(input('Enter a positive number'))
    
    if num>largest:
        largest=num
print("Largest number is:", largest)