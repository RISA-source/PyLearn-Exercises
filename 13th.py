# CSV Reader: Create a program to read and process data from a CSV file.

file = open ('csvReader.csv','w')
file.write('A "Hello, World!" program is generally a simple computer program which outputs (or displays) to the screen (often the console) a message similar to "Hello, World!" while ignoring any user input. A small piece of code in most general-purpose programming languages, this program is used to illustrate a languages basic ')
file.close()

count = {}
file = open ('csvReader.csv','r')
words = file.read()
words = words.split()
for word in words:
    count[word] = count.get(word, 0) + 1
print('The words repeated are shown as follows:')
for k , v in count.items():
    print(k,v)