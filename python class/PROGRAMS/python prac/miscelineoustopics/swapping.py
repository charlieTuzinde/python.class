# A flag variable can be used to let one part of your program know when something happens in
# another part of the program. Here is an example that determines if a number is prime.
num = eval (input ("Enter number:"))

flag = 0 
for i in range (2, num):
    if num%i == 0:
        flag = 1

if flag == 1:
    print ("Not prime")
else:
    print("prime")