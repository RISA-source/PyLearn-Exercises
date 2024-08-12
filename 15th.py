# Basic Calculator: Write a program that functions as a simple calculator.

x = int (input ('Enetr one Number'))
y = int (input ('Enter another Number'))

print('What do you want to perform?')
print('Addition = a \nSubstraction = s \nMultiplication = m \nDivision = d')


oper = input('Enter your Choice....   ')
operd = oper.lower()

if operd != 'a' and operd != 's' and operd != 'm' and operd != 'd':
    print ('Operation not Recognized.')
    quit()

if operd == 'a':
    print ('The sum is: ',x+y)
elif operd == 's':
    print ('The difference is: ',x-y)
elif operd == 'm':
    print ('The multiple is: ', x*y)
else:
    print ('The division is: ',x/y)

print('******************Thank You************************')

