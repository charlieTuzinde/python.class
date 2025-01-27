# This modification of the previous example counts how many of the numbers the user
# enters are greater than 10 and also how many are equal to 0. To count two things we use two count
# variables
count1 = 0
count2 =0
for i in range (10):
    num = eval(input('Enter a number:'))
    if num>10:
        count1=count1+1
    if num==0:
        count2=count2+1
print ('there are ',count1,'numbers greater than 10.')
print ('there are',count2,'zeros.')