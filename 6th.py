# Palindrome Checker: Check if a given string is a palindrome.

s = input ('Enter the string to be checked:')
ps = s.lower()
fs = ''
for i in ps:
    fs = fs + i
if fs == ps:
    print ('The given string is palindrome.')
else:
    print ('The given string is not palindrome.')