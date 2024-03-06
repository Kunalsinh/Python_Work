#Program 5:- Accept one integer value from the user ; display appropriate day of the week;
# weekDays = {
#     1:'Monday',
#     2:'Tuesday',
#     3:'Wednesday',
#     4:'Thursday',
#     5:'Friday',
#     6:'Saturday',
#     7:'Sunday'
# }
# number = int(input('enter Value : '))
# wDaysK = list(weekDays.keys())
# wDaysV = list(weekDays.values())
# print(wDaysK)
# print(wDaysV)
# for i in wDaysK:
#     if(number == i):
#         print('Number is ',i,'and Day of that number is',weekDays[i])
#         break
# print('end of the code!')


#Program 6:- Take Choice from the user and perform the arithmetic operation as per choice.
#choice : 1)Addition 2)Subtraction 3)Multiplication 4)Division
choice = input('Enter choice for the Arithmetic Operation : ')

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