#12.Working with files

#->to open the file we use open() function.
'''
->use 'with as' statement for file handling.
    with expression as variable_name:
        #code
    print('end of the code file.')
->syntax of open() is,
    open(file_path,'mode')
->modes for read,write,append are
    'r' for read
    'w' for write
    'a' for append
->close() method to close the file. 
@->file read methods in python,
    read(size) = worked to read till the end of file.
    readline() = read single line of the file and make it string.
    readlines() = read all lines of the file and make it string.
@->file write methods in python,
    write() = write the data into the file.
    writelines() = write the string of list into the file 
->modes for write,append and for updating (write,read)
    'w' for write
    'a' for append
    '+' for both (write,read)
@->creating file using modes,
    'w' for creating the file if doesn't exist.
    'x' for creating the file is exist then it will give error message
'''

#*]example of read the file using read()... 
# with open('python_notes.txt') as files:
#     content = files.read()
#     print(content)

#*]example of read the file using readline()... 
# with open('python_notes.txt') as files:
#     [print(line) for line in files.readline()]

#*]example of read the file using readlines()... 
# with open('python_notes.txt') as files:
#          [print(lines) for lines in files.readlines()]
         
#*]example of reading file using strip() and readline()...
# with open('python_notes.txt') as files:
#     [print(lines.strip()) for lines in files.readline()]

#*]example of writing data into file using write()...
# lines=['Hello World!','Hi i am from MCA.']
# with open('hello.txt','w') as files:
#     for line in lines:
#         files.write(line)
#         files.write("\n")

#*]example of writing data into file using writelines()...
# lines=['Hiii...','I am from BCA and I am in MCA.']
# with open('hello.txt','w') as files:
#     files.writelines(lines)

#*]example of writing data into file using writelines()
# lines=['Hiii...','I am from BCA .................']
# with open('hello.txt','w') as files:
#     files.writelines('\n'.join(lines))
  
#*]example of appending data into the file using 'a' mode and write()...
# lines=['Roll No','ABCDEFGHIJKL']
# with open('hello.txt','a') as files:
#     files.write('\n'.join(lines))

#*]example of creating a file using 'w' mode and write()...
# with open('hello1.txt','w') as files:
#     files.write('File created!')

#*]example of creating a file using 'x' mode and write()...
# with open('hello1.txt','x') as files:
#     files.write('File created!')
#it will generate the error.

