# Factorial Calculation: Write a program to find the factorial of a number.

n = int (input ('Enter the number:'))
f = 1
for i in range(1, n + 1):
    f = f * i
print ('The factorial is:', f)