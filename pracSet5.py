# Question 1 :-  Create a list containing several strings. Take input from the user (search string);
#               display whether entered string is available in the list or not.

"""listStr = ['hello','user','from','MCA']
userInput = input("Enter user string for search : ")
for i in listStr:
    if(userInput == i):
        print("string matched!",i)
    else:
        print("please exit!")
print("end of the code!")
"""
# Question 2:-  Accept the string from the user; display the message whether the entered string is palindrome or not.

"""palindromeStr = input("Enter a string :")
palin = palindromeStr[::-1]
if(palin == palindromeStr):
    print("It is Palindrome String! ")
else:
    print("It is not Palindrome String! ")
"""

# Question 3 ;- Accept the string from the user; display the string in the reverse order.

"""
simpleStr = input("Enter a string : ")
reversedStr = simpleStr[::-1]
print("Reversed String is ",reversedStr)
"""

# Question 4 :- Accept the string from the user;
#  allow user to choose from the following options and perform the task as per user’s choice.
# i). Convert to the upper case,
# ii). Convert to the lower case,
# iii). Convert to the swap case,
# iv). Convert to the title case

"""
simpleStr = input("Enter a string : ")
options = ["Uppercase","Lowercase","Swapcase","Titlecase"]
print(options)
while(True):
    choice = input("Enter choice from above options :")
    if(choice == options[0]):
        print("String to Upper Case : ",simpleStr.upper())
    elif(choice == options[1]):
        print("String to Lower Case : ",simpleStr.lower())
    elif(choice == options[2]):
        print("String Swap Case : ",simpleStr.swapcase())
    elif(choice == options[3]):
        print("String Title Case : ",simpleStr.title())
    else:
        print("choose valid choice from above options")
        break
"""

# Question 5 :- Allow users to enter multiple strings in the list;
#               arrange the entered string into alphabetical order and display.
""""
strList = []
print("You can store multiple string using space") 
userString=input("Enter multiple strings: ")
stringInput=userString.split()
for x in range(len(stringInput)):
    strList.append(stringInput)
print('List : ',stringInput)
stringInput.sort()
print('Sorted List : ',stringInput)
"""


# Question 6 :- Create a tuple and display it. Enter 25 at the third position and display it again.
"""
numbers = (10,20,60,50,40,70)
print("Tuple numbers : ",numbers)
listNumbers = list(numbers)
listNumbers.insert(3,100)
numbers = tuple(listNumbers)
print("Value added at 3rd index Tuple numbers : ",numbers)
"""

# Question 7 :- Create a dictionary named library with following keys (Bookid, Title, Author, Price, Publisher).
# a. Display the dictionary,
# b. Display the name of Author,
# c. Display the Bookid
# d. Display the length of the dictionary,
# e. Update the price,
# f. Insert year as the new key and display the dictionary again.
"""
library = {
    "Bookid" : 1001,
    "Title" : "Super Human",
    "Author" : "Darshan Maraviya",
    "Price" : 500,
    "Publisher" : "Nikava Gaam"
}
print('Dictionary Library : ',library)
print("Library Author Name : ",library['Author'])
print("Library Bookid : ",library['Bookid'])
print("Length of Library : ",len(library))
library1 = {"Price" : 100}
library.update(library1)
print("Updated Price in Library : ",library['Price'])
print("Inserted New Key and Value : ",library)
"""

# Question 8 :- Create a numeric array and perform following operations on it:
# Add 2 to each elements,
# Subtract 3 from each element,
# Multiply each element with 3,
# Divide each element by 2,
# Find max and min, find the average of all elements.

"""
from numpy import array

numbers = array([10,20,30,40])
print("Numeric Array : ",numbers)
numbersAdded = [x + 2 for x in numbers]
print("Added 2 to each elements :",numbersAdded)
numbersSubtracted = [x - 3 for x in numbers]
print("Subtracted 3 from each elements : ",numbersSubtracted)
numbersDivison = [x / 2 for x in numbers]
print("Divide by 2 : ",numbersDivison)
print("Max Elements from the Array : ",max(numbers))
print("Min Elements from the Array : ",min(numbers))
print("Average of All Elements : ",numbers.mean())
"""

# Question 9 :- Create a numeric array and do the following:
# append the element,
# pop the element,
# insert an element at the desired postion,
# reverse the elements in the array,
# convert the array to list.

"""from array import array
number = array('i',[1,2,3,4,5])
print("Array of Numbers : ",number)
number.append(6)
print("after append an element : ",number)
number.pop()
print("after pop the and element : ",number)
number.insert(3,7)
print("Inserting a element at the specific position 3 : ",number)
number.reverse()
print("Reversed the Array : ",number)
print("Array Converted to List : ",list(number))
"""

# Question 10 :- Accept numeric elements from the user, store it to the array and display.
# Ask user to enter search element. Display the position of the searched element.

"""from array import array
numbers = []
lengthOfArr = int(input("make sure the length of an array : "))
for i in range(lengthOfArr):
    arrValue = int(input("Enter a number : "))
    numbers.append(arrValue)
print("Array is ",array('i',numbers))
search_value = int(input("Enter an element for search it on Array : "))
if(search_value in numbers):
    print("Yes It is founded and the position of that element is ",numbers.index(search_value))
else:
    print("Not Found!")
"""

# Question 11 :- Take two arrays enter 5 digits in both arrays.
# Compare the corresponding element from each array and display only the bigger number.

"""from numpy import array
arrNumber1 = array([10,20,30,40,50])
arrnumber2 = array([50,40,10,70,20])
result = [max(arrNumber1[i],arrnumber2[i]) for i in range(len(arrNumber1))]
print(result)
"""

# Question 12 :-  Accept dimension of the array and its values from the user, create an array as desired.

"""import numpy as np
arrNumbers = []
numbers = int(input("Enter number of elements : "))
for i in range(numbers):    
    numberValues = int(input("Array Element : "))
    arrNumbers.append(numberValues)
print(arrNumbers)
print("Enter Dimension Number of an array : ")
row = int(input("Enter Row : "))
column = int(input("Enter Column : "))
newArr = np.reshape(arrNumbers,(row,column))
print(newArr)
"""

# Question 13 :- Create a function to calculate the simple interest. PRN / 100
"""
def simpleI(percentage,amount,years): 
    simpleInterest = (percentage * amount * years) / 100
    print("Simple Intrest is ",simpleInterest)
per = float(input("Enter percentage for calculate the SI : "))
rate = float(input("Enter amount for calculate the SI : "))
year = float(input("Enter year for calculate the SI : "))
simpleI(per,rate,year)
"""

# Question 14 :- Create a function to perform basic arithmetic operations on the number.
"""
def arithmetic(number1,number2):
    print("-------------------------------------------------------------------------------------")
    print("Addition\t",number1," & ",number2," \tis\t",(number1 + number2)) 
    print("-------------------------------------------------------------------------------------")
    print("Subtration\t",number1," & ",number2,"\tis\t",(number1 - number2))
    print("-------------------------------------------------------------------------------------")
    print("Multiplication\t",number1," & ",number2,"\tis\t",(number1 * number2))
    print("-------------------------------------------------------------------------------------")
    print("Divison \t",number1," & ",number2,"\tis\t",(number1 / number2))
    print("-------------------------------------------------------------------------------------")
num1 = float(input("Enter value for Number1 : "))
num2 = float(input("Enter value for Number2 : "))
arithmetic(num1,num2)
"""

# Question 15 :- Accept multiple strings and store it into the list using function.
"""
def multipleStr():
    simpleStr = []
    Str = input("Enter a string : ") 
    splitStr = Str.split()
    for i in range(len(splitStr)):
        simpleStr.append(splitStr)
    print(splitStr)
multipleStr()
print("end of the code!")
"""

# Question 16 :- Find the biggest number from three values using lambda.

"""
maxValues = lambda num1,num2,num3 : max(num1,num2,num3)
result = maxValues(10,20,40)
print("Maximum Value is",result)
"""

# Question 17 :- Demonstrate the use of: i). break and ii). pass.

"""
numbers = [10,20,30,40,50]
count = 0 
while count < 30:
    print(numbers[count])
    count += 1
    if numbers[count] == 40:
        break
print("End!")

if 1 + 2 == 3:
    print("Done!")
    pass
    print("This will be printed!")
"""
