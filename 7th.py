# Prime Number Checker: Determine if a given number is a prime number.

n = int (input ('Enter the number:'))
for i in range(2,n):
    if n % i == 0 :
        print ('The given number is not a Prime Number.')
        quit()
print ('The given number is prime.')