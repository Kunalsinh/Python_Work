# Program 1: - 
'''
Get the basic salary from the employee and display the net salary by calculating the following conditions: 
Applicable 
TA 4%,
DA 30%, 
HRA 15% on basic salary. 
Applicable 
3% tax,
12% PF on basic salary.
'''

"""
empBasicSalary = int(input("Enter Basic Salary :"))
HRA = (empBasicSalary * 15) / 100
TA = (empBasicSalary * 4) / 100
DA = (empBasicSalary * 30) / 100

PF = (empBasicSalary * 12) / 100
TAX = (empBasicSalary * 3) / 100

netIncome = (empBasicSalary + HRA + TA + DA) - (PF + TAX)
print("Net Salary :",netIncome)
"""  

# Program 2: - get the marks of 5 subjects at the cmd line and display the totaL of marks and percenatage. 

"""
import sys
marksOfSubjects = len(sys.argv)
print("Sum of Command Line Arguments is given below...")

for i in range(1,marksOfSubjects):
    print(sys.argv[i],end= " ",)

sum=0
for i in range(1,marksOfSubjects):
    sum  += int(sys.argv[i])
print("\nSum of all values :",sum)
"""

# Program 3: -
'''
Rajkot Corporation wants to make simple application to calculate Water Bill of Rajkotians. Water is being delivered by the Corporation on per litre charges as below:
Upto 90 litres - Rs. 0/ltr
Upto 150 litres - Rs. 2/ltr
Upto 250 litres - Rs. 5/ltr
More than 250 - Rs. 10/ltr
'''


"""
usedLiters = int(input("Enter how much water used [in liters] :"))
rupees = 0
if(usedLiters < 90):
    print("used water in liters are ",usedLiters,"and charge is ",rupees)
elif(usedLiters < 150):
    rupees = usedLiters * 2
    print("used water in liters are ",usedLiters,"and charge is ",rupees)
elif(usedLiters < 250):
    rupees = usedLiters * 5
    print("used water in liters are ",usedLiters,"and charge is ",rupees)
elif(usedLiters > 250):
    rupees = usedLiters * 10
    print("used water in liters are ",usedLiters,"and charge is ",rupees)
else:
    print("Please enter valid liters")
"""

# Program 4: - 
'''
A tuition class owner wants to make a simple application to allocate grade to the students on the basis of marks student have scored. Accept marks from the students.
Marks more than 90 - A1 grade
Marks 80 or less than or equal 90 - A grade
Marks 70 or less than or equal 80 - B1
Marks 60 or less than or equal 70 - B
Marks 50 or less than or equal 60 - Can do Better!
Marks <50 - Need to work hard.
'''


"""
markOfStudent = int(input("Enter mark of the student :"))
if(markOfStudent > 90):
    print("Student grade : A1 ")
elif(markOfStudent <= 90 and markOfStudent >= 80):
    print("Student grade : A ")
elif(markOfStudent <= 80 and markOfStudent >= 70):
    print("Student grade : B1 ")
elif(markOfStudent <= 70 and markOfStudent >= 60):
    print("Student grade : B ")
elif(markOfStudent <= 60 and markOfStudent >= 50):
    print("Student grade : Can Do Better! ")
elif(markOfStudent < 50):
    print("Neet to work hard.")
else:
    print("Contact your department.")
"""

# Program 5: -
'''
Income Tax department wants to make an application that calculates tax on the basis of the income. Accept yearly income earned by the taxpayer as an input and calculate tax to be paid. The tax slab is as below:
Income up to 8 lakhs - No tax
Income more than 8 lakh and less than 10 lakhs - 15% of income
Income more than 10 lakhs and less than 20 lakhs - 20% of income
Income more than 20 lakhs - 30% of income
'''
"""
yearIncome = int(input("Enter Tax Payer's Yearly Income : "))
if(yearIncome <= 800000):
    tax  = (yearIncome * 0) / 100
    print("No need to pay the tax because your income is less than 8 Lacs")
elif(yearIncome >= 800000 and yearIncome < 1000000):
    tax  = (yearIncome * 15) / 100
    print("You have to pay the tax because your income is ",yearIncome," and payble tax is ",tax)
elif(yearIncome >= 1000000 and yearIncome  < 2000000):
    tax  = (yearIncome * 20) / 100
    print("You have to pay the tax because your income is ",yearIncome," and payble tax is ",tax)
elif(yearIncome >= 2000000):
    tax  = (yearIncome * 30) / 100
    print("You have to pay the tax because your income is ",yearIncome," and payble tax is ",tax)
else:
    print("Done!")

"""


#Program 6: -
'''
Accept two integer values in separate variable, display the small value and big value out of it.
'''
"""
number1 = int(input("Enter Value in Number1 : "))
number2 = int(input("Enter Value in Number2 : "))
print("Number1 is Big and value is ",number1) if number1>number2 else print("Number2 is Big and value is ",number2)
print("Number1 is Small and value is ",number1) if number1<number2 else print("Number2 is Small and value is ",number2)
"""

#Program 7: -
'''
Accept marks from 4 students, display which mark is highest among all.
'''

"""
studentOne = int(input("Enter 1st Student marks"))
studentTwo = int(input("Enter 2nd Student marks"))
studentThree = int(input("Enter 3rd Student marks"))
studentFour = int(input("Enter 4th Student marks"))

if(studentOne > studentTwo and studentOne > studentThree and studentOne > studentFour):
    print("First Student has highest marks.")
elif(studentTwo > studentOne and studentTwo > studentThree and studentTwo > studentFour):
    print("Second Student has highest marks.")
elif(studentThree > studentOne and studentThree > studentTwo and studentThree > studentFour):
    print("Thrid Student has highest marks.")
else:
    print("Fourth Student has highest marks.")
"""    


#Program 8: -
'''
An online selling app wants to develop a application to calculate shipping charges on the purchase.
Accept amount from the user and calculate the shipping charges.
The shipping charges are as below:
Shopping amount less than 1500 - The shipping charges is Rs. 100/-
--Type the message: Please purchase (1500-amount) to avail shipping charge of Rs. 80/-
--Please pay (amount+100)
Shopping amount more than 1500 and less than 3000 - The shipping charges is Rs. 70/-
--Type the message: Please purchase (3000-amount) to avail shipping charge of Rs. 50/-
--Please pay (amount+70)
Shopping amount more than 3000 - Free shipping + 7% discount on amount
--Type a message: You saved (amount*7/100)
--Please pay (amount - discount)
'''

purchase = int(input("Please enter amount :"))

if(purchase < 1500):
    print("Please purchase ",(1500-purchase)," to avail  shipping charges of Rs. 80/-")
    totalBill = purchase + 100
    print("Shipping charge is Rs.100/- So you have to pay ",totalBill," because your purchase is less than 1500.")
elif(purchase > 1500 and purchase < 3000):
    print("Please purchase ",(3000-purchase)," to avail  shipping charges of Rs. 50/-")
    totalBill = purchase + 70
    print("Shipping charge is Rs.70/- So you have to pay ",totalBill," because your purchase is less than 3000.")
elif(purchase > 3000):
    print("You got Free Shiping and 7% Discount on amount becuase your purchase is more than 3000")
    totalBill = purchase - ( purchase * 7 / 100)
    print("You got 7% Discount So you have to pay : ",totalBill)
else:
    print('Please enter valid amount...')