# File Handling: Create a program to read from and write to a text file.

file = open ('readWrite.txt','w')
file.write('This file is automatically created when running the 11th python program.\ngit a')
file.write('This is a subordinate file created by this program for fulfilment of the given task.')
file.close()

file1 = open ('readWrite.txt')
c = file1.read()
print(c)
file1.close()