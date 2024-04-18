import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Question 1:- Create a file with file name sample.txt, accept some data from the user and store it in the file.


"""
file = open('sample.txt', 'w')
userData = input("Enter data to store it into the file : ")
file.writelines(userData)
file.close()
"""

# Question 2 :- Display the data stored in the sample.txt file (created in question 1).

"""
file = open('sample.txt', 'r')
allData = file.read()
print(allData)
file.close()
"""

# Question 3 :- Accept some data from the user and append it into the file sample.txt (created in question 1), also the data in the file.

"""
file = open('sample.txt', 'a')
userAppendData = input("Enter some data to append it into the file : ")
file.write(userAppendData)
file.close()
"""

# Question 4 :- Accept the file name from the user, check the availability of the file:
#    i). If the file exists display the data on the screen,
#    ii). If the file is not available, display the appropriate message.

"""
#import os
getFilename = input("Enter File Name with proper extendsion : ")
if os.path.isfile(getFilename):
    file = open(getFilename, 'r')
    print("File exist!")
    data = file.read()
    print(data)
    file.close()
else:
    print(getFilename+" file does not exist!")
print("End of the code!")
"""

# Question 5 :- Accept the file name from the user, check the availability of the file:
#    a. If the file exists, display:
#       i). No. of characters,
#       ii). No. of words and
#       iii). No. of lines
#    b. If the file does exist, than display the appropriate message.
"""
#import os
filename = input("Enter file name :")
if os.path.isfile(filename):
    print(filename, "File exist!")
    file = open(filename, 'r')
else:
    print(filename, "File does not exist!")

countCharaters = countWords = countLines = 0
for line in file:
    words = line.split()
    countCharaters = countCharaters + len(line)
    countWords = countWords + len(words)
    countLines = countLines + 1
print("Charaters are ", countCharaters)
print("Words are ", countWords)
print("Lines are ", countLines)
"""

# Question 6 :- Create and open the binary file with ‘with’ option. Store names of all the subjects you study in semester 2. Ask user to enter the subject number they wanted to see and display that subject name.
# Yet to complete!
"""
# import mmap
record_length = 10
with open('subjects', 'wb') as file:
    numberOfSubjects = int(
        input("How many subjects you want to store into the file : "))
    for i in range(numberOfSubjects):
        subject_names = input("Enter Subject name : ")
        lengthOfSubjects = len(subject_names)
        subject_names = subject_names + (record_length - 1) * ' '
        subject_names = subject_names.encode()
        file.write(subject_names)
        file.write('\n'.encode())
    file.close()
print("The length of subjects is ", lengthOfSubjects)
userInput = int(
    input("Enter the number from above numbers to get the subject name : "))
with open('subjects', 'rb') as file:
    mapVar = mmap.mmap(file.fileno(), 0)

    if userInput == 1:
        print(mapVar.read().decode())
    else:
        print("nothing")
"""

# Question 7 :- Create a file named ‘img1’, store an image into it. Open another file named ‘img2’, copy the same image as in the file ’img1’. Also store both files into the zip file named ‘imp_img’.
# ywt to complete

# Question 8 :- Create a file with ‘with’ option, name it as ‘marks.dat’.
#    i). Accept subject name and marks from the user, store the data in the file.
#    ii). Give three options to the user: a). To view whole file, b). Accept and edit the marks of a subject user want to change.
#    iii). Exit
"""
import mmap
import sys
with open('marks.dat', 'wb') as file:
    numberOfSubjects = int(
        input("Enter how many subjects you want to enter : "))
    for i in range(numberOfSubjects):
        subjects = input("Enter subject name : ")
        marks = input("Enter marks of that subject : ")
        subjects = subjects.encode()
        marks = marks.encode()
        file.write(subjects + marks)

print("a) To view the whole file ")
print("b) Accept and edit the marks of a subject user want to change ")
print("c) Exit ")

userChoice = input("Enter a choice from the above option either a , b or c : ")

if userChoice == 'c':
    sys.exit()
with open('marks.dat', 'r+b') as file:
    mapVar = mmap.mmap(file.fileno(), 0)

if userChoice == 'a':
    print(mapVar.read().decode())

if userChoice == 'b':
    subjectToBeChange = input("Enter subject name to change it's marks : ")
    getSubjectName = mapVar.find(subjectToBeChange.encode())
    subjectLength = getSubjectName+len(subjectToBeChange)
    getNewMarks = input("Enter modified marks : ")
    marks = mapVar[subjectLength:subjectLength+3] = getNewMarks.encode()
file.close()
"""

# Question 9 :- Create a regular expression that:
#    a). Identifies and display the string starting with ‘s’ and having 4 characters.
#    b). Splits the string where some special characters are found.
#    c). Display the word starting with number.
#    d). Display the word having 3 or 4 or 5 characters.
#    e). Display only the dates from the string.
#    f). Create a string with name of the person and his Aadhar number, display only Aadhar number.
#    g). Display all the words that starts with ‘at’ or ‘ap’.
#    h). Check if the string starts with ‘at’ than display appropriate message and otherwise.
"""
import re
normalString = "sun 45son ! atmiya appear application atom suns snoop on 12-01-1998!"
person = "Rohit Sharma atmiya 7485-9632-1021"

resultA = re.findall(r's\w\w\w\w', normalString)
print("a => ", resultA)

resultB = re.split(r'\W+', normalString)
print("b => ", resultB)

resultC = re.findall(r"\d[\w]*", normalString)
print("c => ", resultC)

resultD = re.findall(r'\b\w{3,5}\b', normalString)
print("d => ", resultD)

resultE = re.findall(r'\d\d-\d\d-\d{4}', normalString)
print("e => ", resultE)

resultF = re.findall(r'\d{4}-\d{4}-\d{4}', person)
print("f => ", resultF)

resultG = re.findall(r'a[tp][\w]*', normalString)
print("g => ", resultG)

resultH = re.search(r'^at', person)
if resultH:
    print("Yes string have some words start with 'at'.")
else:
    print("No string have not any words start with 'at'.")
"""
# Question 10 :- Do as directed:
#    a). Name the package used to deal with data frame. [pandas]
#    b). Name the package used to deal with data .xlsx file. [xlrd]
#    c). Name the function used to read the .csv file. [read_csv()]
#    d). Name the function used to read the .xlsx file. [read_excel()]
#    e). Name the function used to read the tuple. [tuple()]

# Question 11 :- Create a dictionary which stores (at least 10 records)empid, name, city, salary and perform
# following operations:
#    a). Display first three records
#    b). Display last five records
#    c). Display only Name and City
#    d). Display employee who belongs to Mumbai
#    e). Display employee name who belongs to Mumbai
#    f). Display employee whose salary is more than 25000

"""
#import pandas as pd
employee = {
    "empid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "name": ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZ', 'HELLO'],
    "city": ['Rajkot', 'Porbandar', 'Kashmir', 'Jammu', 'Raigadh', 'Indore', 'Mumbai', 'Ahemdabad', 'Surat', 'Diu'],
    "salary": ['10000', '20000', '30000', '40000', '50000', '60000', '70000', '80000', '90000', '100000']
}
resultA = pd.DataFrame(employee)
print("a => ", resultA)
print("--------------------------------------------------------")
print("b => ", resultA.head(3))
print("--------------------------------------------------------")
print("c => ", resultA.tail(5))
print("--------------------------------------------------------")
print("d => ", resultA[['name', 'city']])
print("--------------------------------------------------------")
mumbaiData = resultA[resultA['city'] == 'Mumbai']
print("e => ", mumbaiData)
print("--------------------------------------------------------")
mumbaiDataName = resultA.loc[resultA['city'] == 'Mumbai', 'name']
print("f => ", mumbaiDataName)
print("--------------------------------------------------------")
moreThan25k = resultA[resultA['salary'] > '25000']
print("g => ", moreThan25k)
"""

# Question 12 :- Create an xlsx file store marks of five subjects, plot the data on the bar graph.
"""
dataframe = pd.read_excel('data12.xlsx')
print(dataframe)

x = dataframe['Subjects']
y = dataframe['Marks']

plt.bar(x, y, label="Result of Student", color="lightblue")

plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.title("Result")

plt.legend()
plt.show()
"""
# Question 13 :- Take five income source of the Government and display it on the pie chart.

"""
percentage = [12, 40, 24, 10, 34]
incomeSource = ['IT_Cell', "IT_Technology", "Culture", "GST", "Tax"]
col = ['blue', 'black', 'lightgreen', 'green', 'gray']

plt.pie(percentage, labels=incomeSource, colors=col)
plt.title("Government Sources")
plt.legend()
plt.show()
"""

# Question 14 :- Draw the line chart representing BSE (Bombay Stock Exchange) index in last 10 years.

"""
years = ['2011', '2012', '2013', '2014', '2015',
         '2016', '2017', '2018', '2019', '2020']
incr_index = [45, 78, 98, 45, 65, 75, 74, 63, 89, 15]
plt.plot(years, incr_index, color='blue')
plt.title('Bombay Stock Exchage Indexing last 10 years')
plt.xlabel("Years")
plt.ylabel("Indexing")
plt.legend()
plt.show()
"""

# Question 15 :- Plot the grouped bar graph using the appropriate data.

year = [2023, 2022, 2021]

pencil = [20000, 10000, 11000]

pen = [15000, 12000, 9000]

x_axis = np.arange(len(year))

plt.bar(x_axis - 0.2, pencil, label='Pencil Sale', color="Blue", width=0.3)
plt.bar(x_axis + 0.2, pen, label='Pen Sale', color="Gray", width=0.3)

plt.xticks(x_axis, year)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Stationery')
plt.legend()
plt.show()
