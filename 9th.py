# Armstrong Number: Check if a given number is an Armstrong number.

n = input ('enter the number to be checked:')
fp = 0
try:
    ni = int(n)
except:
    print('Given input is not a number.')
    quit()
l = len (n)
for i in n:
    fp = fp + int(i) ** l
if fp == ni :
    print('The given number is armstrong')
else:
    print('The given number is not armstrong.')
