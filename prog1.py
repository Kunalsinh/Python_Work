#simple print hello using print() in-built function.and 
#print('Hello')

#Topic 1 : Different type of variable assigning 
# 1)Single variable and single value
'''

name='Kunalsinh'
surname='Solanki'
print('Fullname : ',name,surname)

'''
    #=>above we use multi line comment [three single line comment sign]

# 2)different variable but value will be same
"""

num1=num2=10
print('Number1 Variable :',num1) #output 10
print('Number2 Variable :',num2) #output 10

"""
# 3)different variable and different value but on same line.
'''

num1,num2=20,30
print('Number1 Value is',num1) #output 20
print('Number2 Value is',num2) #output 30

'''
    #=> above we can do variable declaration and assigning value on same line.

#Topic 2: String format using module % sign
""" 

city='Rajkot' # length is 6 characters

print('City is ',city) # simple output
print('City is %s'%city) # simple output

print('City is %20s'%city) #output ______________Rajkot
'''
Explanation:-
-> here total space will be 20 characters
-> then city variable's value will be print AFTER 14 characters space. 
-> above output is only for example
'''

print('City is %-20s'%city) #output Rajkot______________
'''
Explanation:-
-> here total space will be 20 characters
-> then city variable's value will be print BEFORE 14 characters space. 
-> above output is only for example
'''

"""

#Topic 3: Place Holders
"""

num1 = 22
num2 = 11
print('1)Three values are {0},{1} & {0}'.format(num1,num2)) # output 22,11 & 22
print('2)Three values are {0},{1} & {0}'.format(num2,num1)) # output 11,22 & 11

'''
Explanation:-
-> Here place holder index start from 0 and we have to consider .format() for giving index 
-> 1)Here 0th index means num1 variable and 1st index means num2 variable
-> 2)Here 0th index means num2 variable and 1st index means num1 variable
'''

"""

#Topic 4: Use of type() in-built function
'''

name='Kunalsinh'
age=10
print('Datatype of variable name is ',type(name))
print('Datatype of variable age is ',type(age))

'''

#Topic 5: getting input from user using input()
'''

#simple user input
word = input('Enter any word :')
print(word)

#use str() for String value only [for string we have to put some condition also because anything can be string]

uname = str(input('Enter University Name :'))
print('Output of uname variable is',uname)

#use int() for Integer value only

randomNum = int(input('Enter Random Number :'))
print('Output of randomNum variable is',randomNum)

'''