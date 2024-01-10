#Practice Set 1


#Write a program that prints  your name and university name .

print('\nName is Kunalsinh A Solanki University name is Atmiya University')

#Write a program that prints your address with name , all in new lines.

name = 'Kunalsinh A. Solanki'
address = 'Nanavati Chowk, Rajkot, Gujarat.'
print('\nName : ',name,'\nAddress : ',address)

#Write a program that accepts two numbers and perform all aerithmetic operations.

num1 = 10 
num2 = 5

print('\nAddition',(num1+num2))
print('\nSubtraction',(num1-num2))
print('\nMultiplication',(num1*num2))
print('\nDivision',(num1/num2))

# Write a Program to calculate simple interest.
interest=0
profit=10000
roI = 20
noY = 4

interest = (profit * roI * noY) / 100
print('\nInterest is ',interest)

#Write a program to calculate 10% of bonus on salary.

salary = 25000
bonus = (salary * 10 / 100)
print('\nBonus is ',bonus)

#Write a program to calculate KM into Meter.

numberKM = 35
meter=0

meter = numberKM * 1000
print('\nKM into Meter is',meter)

# The distance between two cities is input through keyboard. write a program to convert and print this distance in feet, meter, inch and centimeter

distance=float(input('Enter Distance between two cities :'))
feet = (distance * 3280.84)
meter = (distance * 1000)
inch = (distance * 39370.1)
centimeter = (distance * 100000.54)

print('\nDistance is ',distance)
print('\nDistance in Feet is ',feet)
print('\nDistance in Inch is ',inch)
print('\nDistance in Meter is  ',meter)
print('\nDistance in Centimeter is ',centimeter)

#Use place holder to print above output as it is. 

print('\nDistnace is {0} \nDistance into Feet : {1} \nDistance into Inch : {2} \nDistance into Meter: {3} \nDistance into Centimeter: {4}'.format(distance,feet,inch,meter,centimeter))

