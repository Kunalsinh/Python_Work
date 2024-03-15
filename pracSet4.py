#Program 1:- Accept two integer values from the user; display the number which is smaller and the number which is bigger.

"""number1 = int(input('Enter value for Number1 : '))
number2 = int(input('Enter value for Number2 : '))
print('Number1',number1,'is Big and Number2',number2,'is Small.') if number1 > number2 else print('Number2',number2,'is Big and Number1',number1,'is Small.')
"""

#Program 2:- Accept one integer value from the user; check whether entered number is divisible by 5 or not.
"""
number = int(input('Enter value for Number : '))
print('Yes, Number is Divisible by 5.') if number % 5 == 0 else print('No, Number is not Divisible by 5.')
"""

#Program 3:- Accept one integer value from the user; check whether entered number is between 0-100 or not.
"""
number = int(input('Enter value for Number : '))
print('Yes, Number',number,'is between 0-100.') if (number > 0 and number <= 100) else print('No, Number',number,'is not between 0-100.')
"""

#Program 4 :- Accept one integer value from the user; display the length of the entered number, also display that the entered number is of four digits or not. 
"""
number = int(input('Enter integer value : '))
lengthOfNumber = len(str(number))
print('Length of Number is ',lengthOfNumber)
print('Yes,Number has four digits and it is four digits integer value.') if (lengthOfNumber == 4) else print('No,Number not has four digits in it.')
"""

#Program 5:- Accept one integer value from the user; display appropriate day of the week.
"""
weekDays = {
    1:'Monday',
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday'
}
number = int(input('Enter a number from 1 to 7 : '))
wDaysKey = list(weekDays.keys())
wDaysValue = list(weekDays.values())
print('Week Days :',wDaysValue)
for i in wDaysKey:
    if(number == i):
        print('Number is ',i,'and Day of that number is',weekDays[i])
        break
print('end of the code!')
"""

#Program 6:- Take Choice from the user and perform the arithmetic operation as per choice.
#choice : 1)Addition 2)Subtraction 3)Multiplication 4)Division
"""
arithmetic = ['Addition','Subtraction','Multiplication','Division']
print(arithmetic)
choice = input('Enter a choice from the above Arithmetic Operations : ')

number1 = int(input('Enter Value for Number1 : '))
number2 = int(input('Enter Value for Number2 : '))

def addition():
    result = number1 + number2
    print('Addition :',result)
def subtraction():
    result = number1 - number2
    print('Subtraction :',result)
def multiplication():
    result = number1 * number2
    print('Multiplication :',result)
def division():
    result = number1 / number2
    print('Division :',result)

if(choice == 'Addition'):
    addition()
elif(choice == 'Subtraction'):
    subtraction()
elif(choice == 'Multiplication'):
    multiplication()
elif(choice == 'division'):
    division()    
else:
    print('Please enter valid choice...')
"""

#Program 7:- Accept the string from the user; display the count of vowels and consonants.

"""
count = 0
userString = input("Enter any string : ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
for char in userString:
    if char in vowels:
        count = count + 1
print('No. of Vowels is ',count)
consonent = len(str(userString)) - count
print('No. of Consonent :',consonent)
"""

#Program 8:- Accept one integer value from the user; display the table of it.
"""
number = int(input('Enter any number :'))
for i in range(1,11):
    print(number,'*',i,'=',(number*i))
print('end of the code.')
"""

#Program 9:- Display square and cube of numbers 1-10.
"""
for i in range(1,11):
    print('Square of ',i,'=',i**2,'\tand\t','Cube of ',i,'=',i**3)
print('end of the code.')
"""

#Program 10:- Accept string from the user; convert the string to upper case.
"""
userString = input('Enter any string : ')
print('Actual String :',userString,' \tand\t String in Uppercase : ',userString.upper())
"""

#Program 11:- Display the following output using loop:
# i. 1 to 10
# ii. 10 to 1
# iii. 1 3 5 7 9
# iv. 2 4 6 8 10

"""
print('i.Number 1 to 10 :')
for i in range(1,11):
    print(i,end=" ")
print('\nii.Number 10 to 1 :')
for i in range(10,0,-1):
    print(i,end=" ")
print('\niii.Number Odd Only :')
for i in range(1,11,2):
    print(i,end=" ")
print('\niv.Number Even Only :')
for i in range(2,11,2):
    print(i,end=" ")
"""

#Program 12:- Print 1 2 4 8 16 32 64 128 256 512 1024
"""
print('Print 1 2 4 8 16 32 64 128 256 512 1024')
count = 1
while(count <= 1100):
    print(count,end=' ')
    count+=count
print('\nend of the code.')
"""

#Program 13:- Accept the number from the user; display the table of that number.
#same as Program 8.

#Program 14:- Accept numbers from the user; display the sum of the entered numbers.

"""
number = input("Enter Numbers : ")
sum = 0
for i in str(number):
    sum += int(i)
print('Sum of numbers : ',sum)
"""

#Program 15:- Accept numbers from the user; display the count of the entered numbers.
"""
number = input("Enter Numbers : ")
print(len(number))
"""
#incomplete!

#Program 16:- Accept numbers from the user; find and display number of zeros available in the number.
"""
number = input("Enter Numbers : ")
count = 0 
for i in str(number):
    if(i == '0'):
        count+=1
print('Number is ',number,'\tand\t Zeros are',count)
"""

#Program 17:- Accept an integer from the user; tell user that whether entered number is even or odd.
# Required output:
# Enter the number: 7
# 7 is an odd number
# Do you want to check another number? Y
# Enter the number: 2
# 2 is an even number
# Do you want to check another number? N

"""
def EvenOdd():    
    number = int(input('Enter any number : '))
    if(number % 2 == 0):
        print('Number is',number,'and it is an Even Number!')
        choiceEO()
    else:
        print('Number is',number,'and it is an Odd Number!')
        choiceEO()

def choiceEO():
    choice = input('Do you want to check another number? [Yes/No] : ')
    if(choice == 'Yes'):
        EvenOdd()
    elif(choice == 'No'):
        print('End of the code.')

EvenOdd()
"""