# The following program prints Tuzinde a random number of times between 5 and 25.   (this is a for loop)
from random import randint 
# IMPORTS ANY RANDOM NUMBER TO USE
rand_num = randint (5,25)
# this specifies that the random number chosen has to be only between 5 and 25
for i in range (rand_num):
    # for i in range      specifies what the program should now do
    print ("Tuzinde")
    # output is Tuzinde* any nu mber btwn 5/25