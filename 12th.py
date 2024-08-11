# Word Counter: Write a program to count the number of words in a text file.

file = open ('countfile.txt','w')
file.write('The lorem shortcut! Open your HTML page in VSCode, point to the part where you want to add some random text, write this: lorem5 and press Tab What just happened? 5 words have been added to your HTML just like that. Now you can save precious seconds, or minutes even, with this shortcut!')
file.close()

file = open ('countfile.txt','r')
c = file.read()
cs = c.split()
words = len(cs)
print ('The number of words are:', words)
file.close()