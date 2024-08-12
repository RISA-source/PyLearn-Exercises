# Student Grade Management: Create a program to manage student grades, including adding, updating, and displaying grades.

d = dict()
print('Operations Available: \n1. Add New Student and Grades \n2. Update the grades of existing Student\n')
w = int(input('Enter one of the choices: '))

def opt1():
    n = int (input ('Enter the number of records you want to add:'))
    for i in range(n):
        stdName = input('Enter the name of student:')
        stdGrades = int (input('Enter the grade of student (%): '))
        d[stdName] = stdGrades

    for n , g in d.items():
        print (n,g,'%')

def opt2():
    n = int (input ('Enter the number of records you want to Update:'))
    for i in range (n):
        stdName = input('Enter the name of student:')
        stdGrades = int (input('Enter the grade of student (%): '))
        d[stdName] = stdGrades
    
    for n , g in d.items():
        print (n,g,'%')

if w == 1:
    opt1()
elif w == 2:
    opt2()
else:
    print('The option doesnot exist.')
    quit()



