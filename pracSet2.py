#Program 1 : Find Area of the Triangle

'''
baseOfT = float(input('Enter Base of Triangle :'))
heightOfT = float(input('Enter Height of Triangle :'))

areaTriangle = ((baseOfT * heightOfT) / 2)
print('Area of Triangle :', areaTriangle)
'''

#Program 2 : Find Area of Squaree 

'''
heightS = float(input('Enter Height of Square :'))
widthS = float(input('Enter Width of Square :'))

areaSquare = heightS * widthS
print('Area of Square :',areaSquare)
'''

#Program 3 : Write a program to convert Celcius to Ferenhit.

'''
celsiusNumber = float(input('Enter Celcius Number :'))
convertedFahrenheit = (celsiusNumber *  (9/5) + 32) 
print('Celsius into Fahrenheit :',convertedFahrenheit)
'''

#Program 4: Convert US Dollar  to Indian Rupees 

'''
indianRuppe = 82.88
usDollarR = int(input('Enter US Dollar :'))
convertedRupees = (usDollarR * indianRuppe)
print('US Dollar convertetd to Indian Rupees :',convertedRupees)
'''

#Program 5 : Convert Litter to MiliLitter

'''
Litter = float(input('Enter How much Littler you want to be convertetd into MiliLitter :'))
MiliLitter = 1000
convertedML = (Litter * MiliLitter)
print('Litter to MiliLitter',convertedML)
'''

#Program 6 : Enter binary, octal and hexadecimal values and convert it into decimal.

'''
numberBinary = 0b1100
numberOctal = 0o16
numberHexadecimal = 0xa

print('Binary to Decimal :',int(numberBinary))
print('Octal to Decimal :',int(numberOctal))
print('Hexadecimal to Decimal :',int(numberHexadecimal))
'''

#Program 7 : Accept one integer value from the user; convert it to binary, octal and hexadecimal.

'''
numberInt = 452

print('Decimal to Binary :',bin(numberInt))
print('Decimal to Octal :',oct(numberInt))
print('Decimal to Hexadecimal :',hex(numberInt))
'''

#Program 8 : Accept string from the user (‘The Rajkot is a good city to leave’), and do the following operations: 
             #i). Display the first character of the string, 
             #ii). Display the first character of the string using negative index, 
             #iii). Display ‘Rajkot is a good city’. 
             #iv). Display the last character.
'''
sentence = 'The Rajkot is a good city to leave'
print('Display the first character of the string :',sentence[0])
print('Display the first character of the string using negative index[-34] :',sentence[-34])
print('Display ‘Rajkot is a good city’ :',sentence[4:25])
print('Display the last character :',sentence[-1])
'''

#Program 9 : Create bytes, enter some values and display all elements.

'''
number = 10
numberByte = bytes(number)
print('Display Bytes :',numberByte)
'''

#Program 10 : Create bytearray, enter some values and perform the following: 
              #i). Replace the 3rd element with 7, 
              #ii). Display the 5th element.
'''
number = [1,2,3,4,5,6,7,8,9,10]
numberByteArr = bytearray(number)
print(numberByteArr)
print('Before Changed :',numberByteArr[3])
numberByteArr[3] = 7
print('After Changed :',numberByteArr[3])
print('5th Element of Byte Array :',numberByteArr[5])
'''

#program 11 : Create list and insert values. 
            #i).Display all the elements. 
            #ii). Display the 3rd element,
            #iii). Replace the 4th element with ‘Atmiya’, 
            #iv). Display elements from 3rd to 7th element.
'''
names = ['Amit','Ambrish','Jayesh','Jaydeep','Rajesh','Abhisek','Suraj','Ramesh','Rakesh','Naman','Kirit']
print('All elements of List names :',names)
print('Display the 3rd element of List :',names[3])
print('Before 4th element changed :',names[4])
names[4] = 'Atmiya'
print('Display 4th element After :',names[4])
print('Display elements from 3rd to 7th elements :',names[3:8])
'''

#Program 12 : Create tuple and insert values. 
              #i). Try to replace the 3rd element with 9 
              #ii). Display the 5th element.
'''
numberTuple = (1,2,3,4,5,6,7,8,9,10)
print('Tuple number :',numberTuple)
print('Display the 5th element :',numberTuple[5])
'''

#Program 13 : Create a set insert some values. 
              #i). Add elements to it and display 
              #ii). Remove elements from it and display.
'''
numbers = set(['One','Two','Three','Four'])
print('Set numbers :',numbers)
numbers.add('Five')
print('Added Element :',numbers)
numbers.remove('Four')
print('Remove Element :',numbers)
'''

#Program 14 : Create a set insert some values and convert it to frozenset. Try to add and remove some elements.
'''
numbers = set(['One','Two','Three','Four'])
print('Set numbers :',numbers)
numberFrozen = frozenset(numbers)
print('Frozen Set :',numberFrozen)
#given below code will generate the error that we can't add any element into frozen set.
numberFrozen.Add('Six')
print('Added to FrozenSet :',numberFrozen)
'''

#Program 15 : Create an empty dictionary, Insert some Roll:Name into it. 
             #i). Retrieve 5th value using key 
             #ii). Retrieve all the roll numbers 
             #iii). Retrieve all the names 
             #iv). Change the name of the student having roll no. 7 
             #v). Remove roll no 9, 
             #vi). Display the dictionary
'''

numberStudent = int(input('How many student you want to put it into list :'))
students = {}
for i in range(numberStudent):
    rollnos = int(input('Enter Roll No :'))
    names = input('Enter Name :')
    students[rollnos] = [names]
print('\nDictionary :',students)
print('\n5th Value of Dictionary :',students[5])
print('\nAll the roll no from Dictionary :',students.keys())
print('\nAll the names from Dictionary :',students.values())
students.update({7:'Darshan'})
print('Updated Dictionary :',students)
del students[9]
print('After Deletation of 9th RollNo :',students)
'''

#Program 16 : Create a list having names of months. 
            #i). Check whether December is in list or not, 
            #ii). Query the list using ‘not in’.
'''
months  = ['January','February','March','April','May','June','July','Augest','September','October','November','December']
print('Months of Year :',months)
print("\nDecember" in months)
print('\nJanmber' not in months)
'''

#Program 17 :Take two integer values from the user using split(), perform basic arithmetic operation on the values.
'''
num1,num2=input('Enter A Value :').split()
print('Value of Num1 :',num1)
print('Value of Num2 :',num2)
total = int(num1) + int(num2)
print("Total is ",total)
'''
