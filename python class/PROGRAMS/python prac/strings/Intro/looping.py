'''Very often we will want to scan through a string one character at a time. A for loop like the one
below can be used to do that. It loops through a string called s, printing the string, character by
character, each on a separate line:
'''

s=input('enter some type of a word')
# for i in range(len(s)):
#     print(s[i])
    '''In the range statement we have len(s) that returns how long s is. So, if s were 5 characters long,
this would be like having range(5) and the loop variable i would run from 0 to 4. This means
that s[i] will run through the characters of s. This way of looping is useful if we need to keep
track of our location in the string during the loop'''
    """"""
#If we don’t need to keep track of our location, then there is a simpler type of loop we can use:
s = input('Enter a string')
for c in s:
print(c)