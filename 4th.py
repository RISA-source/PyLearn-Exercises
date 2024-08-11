# Simple Interest Calculator: Create a program to calculate simple interest.

p = int (input ('Enter the Principle amount:'))
t = int (input ('Enter the Time period:'))
r = int (input ('Enter the Rate of Interest:'))
i = (p * t * r) / 100
print ('The simple interest amounts to:',i)