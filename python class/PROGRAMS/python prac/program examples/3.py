from random import randint
for i in range(6):
    rand_num = randint(1,5)
    print('Tuzinde'*rand_num)

    """The only difference between the programs is in the placement of the rand_num statement. In
the first program, it is located outside of the for loop, and this means that rand_num is set once
at the beginning of the program and retains that same value for the life of the program. Thus
every print statement will print Hello the same number of times. In the second program, the
rand_num statement is within the loop. Right before each print statement, rand_num is assigned a
new random number, and so the number of times Hello is printed will vary from line to line.
"""