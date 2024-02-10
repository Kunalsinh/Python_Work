# Program 1: - Get the basic salary from the employee and display the net salary by calculating the following conditions:

# Add Applicable
# a.TA 4% 
# b.DA 30%
# c.HRA 15%  

# Deduct Applicable
# a. 3% Tax (200)
# b.12% PF on basic salary.

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

import sys
marksOfSubjects = len(sys.argv)
print("")

# Program 3: - RMC wants to make simple application to calculate water bill of rajkotians.
#              water is being deliverd by RMC on per liter charges as below.
# up to 90 liters - 0/lt
# up to 150 liters - 2/lt
# up to 250 liters - 5/lt
# more than 250 liters - 10/lt
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

# Program 4: -  A Tuition class owner wants to make a simple application to allocate
#grade to the students oon the basic of marks student and have scored. Accept marks from the students.
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

# Program 5: - IT Department wants to make an application that calculates tax on the basis of the income.
# Accept yearly income earned by the taxpayer as an input and calculate tax to be paid.
# income up to 8 lacs - no tax 
# income > to 8 lacs  and < 10 lacs - 15% of income  
# income >  10 lacs and < 20 lacs - 20% income 
# income> 20 lacs - 30% income

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

