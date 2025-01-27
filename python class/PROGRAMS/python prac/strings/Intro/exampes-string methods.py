"""s=("Tuzinde")
print(s.count(''))"""
# 2
"""s=("Tuzinde")
s=s.upper()"""



s = input('Enter a string')

if s[0].isalpha():
    print('Your string starts with a letter')
if not s.isalpha():
    print('Your string contains a non-letter.')