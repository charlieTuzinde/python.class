# for picking out individual characters



# SLICES
"""A slice is used to pick out part of a string. It behaves like a combination of indexing and the range
function  
• The basic structure is
string name[starting location : ending location+1]

Slices have the same quirk as the range function in that they do not include the ending
location. For instance, in the example above, s[2:5] gives the characters in indices 2, 3, and
4, but not the character in index 5
• We can leave either the starting or ending locations blank. If we leave the starting location
blank, it defaults to the start of the string. So s[:5] gives the first five characters of s. If
we leave the ending location blank, it defaults to the end of the string. So s[5:] will give
all the characters from index 5 to the end. If we use negative indices, we can get the ending
characters of the string. For instance, s[-2:] gives the last two characters.
• There is an optional third argument, just like in the range statement, that can specify the step.
For example, s[1:7:2] steps through the string by twos, selecting the characters at indices
1, 3, and 5 (but not 7, because of the aforementioned quirk). The most useful step is -1, which
steps backwards through the string, reversing the order of the characters.

"""
# 6.6 Changing individual characters of a string
"""Here is code that will change the character at index 4 to 'X':"""
s = input('Enter a string')
s = s[:4] + 'x' + s[5:]

'''The idea of this is we take all the characters up to index 4, then X, and then all of the characters
after index 4.'''