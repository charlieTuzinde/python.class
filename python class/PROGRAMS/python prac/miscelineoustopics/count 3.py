count = 0
for i in range (1,101):
    if (i**2)%10==4:
        count = count + 1
print (count)
# quares from 1squared# to 100squared
# end in a 4.

# A few notes here: First, because of the aforementioned quirk of the range function, we need to use
# range(1,101) to loop through the numbers 1 through 100. The looping variable i takes on those
# values, so the squares from 1
# 2
# to 1002
# are represented by i**2. Next, to check if a number ends
# in 4, a nice mathematical trick is to check if it leaves a remainder of 4 when divided by 10. The
# modulo operator, %, is used to get the remainder.