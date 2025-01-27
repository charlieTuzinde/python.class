for i in range (len (s)) :
    print (s[int])
    
    """In the range statement we have len(s) that returns how long s is. So, if s were 5 characters long,
this would be like having range(5) and the loop variable i would run from 0 to 4. This means
that s[i] will run through the characters of s. This way of looping is useful if we need to keep
track of our location in the string during the loop.
If we dont need to keep track of our location, then there is a simpler type of loop we can use"""

for c in s:
print(c)

"""This loop will step through s, character by character, with c holding the current character. You can
almost read this like an English sentence, “For every character c in s, print that character.”
"""