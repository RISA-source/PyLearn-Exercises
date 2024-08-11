# Fibonacci Series: Generate the first n numbers in the Fibonacci series.

n = int (input('Enter how many fibonacci numbers you want?'))
a = 0
b = 1
c = 0
for i in range(n):
    print(c)
    c = a + b
    a = b
    b = c
