#1) Open a file
#file = open("example.txt", "r")

#2) Read the contents of a file
#file = open("example.txt", "r")

#3) Write to a file
#file = open("example.txt", "w")

#4) Append to a file
#file = open("example.txt", "a")

#5) Close a file
#file.close()

#6) Read all lines from a file
#file = open("example.txt", "r")
#lines = file.readlines()
#file.close()

#7) Read a file line by line
#file = open("example.txt", "r")
#for line in file:
#    print(line)
#file.close()

#8) Write multiple lines to a file
#file = open("example.txt", "w")
#file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
#file.close()

#9) Check if a file exists
#import os
#if os.path.exists("example.txt"):
#    print("File exists")
#else:
#    print("File does not exist")  

#10) Delete a file
#import os
#os.remove("example.txt")

#11) Rename a file
#import os
#os.rename("example.txt", "new_example.txt")

#12) Get the size of a file
#import os
#size = os.path.getsize("example.txt")
#print(f"File size: {size} bytes")

#13) Copy a file
#import shutil
#shutil.copy("example.txt", "copy_example.txt")

#14) Move a file
#import shutil
#shutil.move("example.txt", "new_location/example.txt")

#15) Read a file and count the number of lines
#file = open("example.txt", "r")
#lines = file.readlines()
#count = len(lines)
#print(f"Number of lines: {count}")
#file.close()

#16) Read a file and count the number of words
#file = open("example.txt", "r")
#content = file.read()
#words = content.split()
#count = len(words)
#print(f"Number of words: {count}")
#file.close()

#17) Read a file and count the number of characters
#file = open("example.txt", "r")
#content = file.read()
#count = len(content)
#print(f"Number of characters: {count}")
#file.close()

#18) Read a file and count the number of occurrences of a specific word
#file = open("example.txt", "r")
#content = file.read()
#count = content.count("specific_word")
#print(f"Number of occurrences: {count}")
#file.close()

#19) Read a file and print its contents in reverse order
#file = open("example.txt", "r")
#lines = file.readlines()
#lines.reverse()
#for line in lines:
#    print(line)
#file.close()

#20) Read a file and print its contents in uppercase
#file = open("example.txt", "r")
#content = file.read()
#print(content.upper())
#file.close()

#21) Read a file and print its contents in lowercase
#file = open("example.txt", "r")
#content = file.read()
#print(content.lower())
#file.close()