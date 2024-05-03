# unit 5 Data Science
# data science tools and libraries
# Pandas

# 1.Working with .csv file using pandas
import pandas as pd
df = pd.read_csv('student.csv')  # put csv file into ()
print(df)

# 2.Working with .xlsx file using pandas
# Creating data frame from .xlsx files
# in terminal :-
# py -m pip install xlrd
# py -m pip install openpyxl
'''
import pandas as pd
import xlrd 
df = pd.read_excel() #put .xlsx file into ()
print(df)
'''

# Working with python dictionary using pandas
# Creating data frame from python directory

'''
student = {
    'rollno':[1,2,3,4,5],
    'name':['ABC','DEF','GHI','JKL','MNO'],
    'city':['Rajkot','Surat','Goa','Diu','Daman']
}
import pandas as pd
df = pd.DataFrame(student)
print(df)
'''

# Wroking with python tuple using pandas
# creating data frame from tuples

'''
student  = [{"ABC","Rajkot"},{"DEF","Diu"},{"GHI","Goa"}]
import pandas as pd
df = pd.DataFrame(student)
print(df)
'''

# Knowing number of rows and columns
'''import pandas as pd
import xlrd
df = pd.read_excel('stud.xlsx')
print(df)
print(df.shape)
print(df.head)
print(df.head(2))
print(df[['Name','City']])
print(df['Marks'].min)
print(df['Marks'].max)
print(df[df.City == 'Rajkot'])
print(df[df.Marks > 50])
#Display the name of the student who belongs to surat.
print(df[['Name','Roll']][df.City == 'Surat'])
'''

# Handling the missing data

'''
import pandas as pd
import xlrd

df = pd.read_excel('stud.xlsx')
print(df)
new = df.fillna({'Name':'Name is missing','MobileNo':'Mobile No is missing'})
print(new)
'''

# Data Visualization
# Requires 'matplotlib'
# Bar Graph

'''import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('book.xlsx')
print(df)

#Extracting the type_of_book and sales into x and y
x = df['Types_Of']
y = df['Sales']

#Creating the bar using bar()
plt.bar(x,y,label='Category wise Sales of Book',color='lightblue')

#Settings the label of x-axis and y-axis
plt.xlabel('Types of Books')
plt.ylabel('Sales in ₹')

#Settings the title of the ownership
plt.title('Atmiya Book Stall')

#show the legend 
plt.legend()

#display the graph
plt.show()
'''

# Bar graph of that data
"""
import matplotlib.pyplot as plt 
import numpy as np

year = [2023,2022,2021]

pencil = [20000,10000,11000]

pen = [15000,12000,9000]

x_axis = np.arange(len(year))

plt.bar(x_axis - 0.2 ,pencil,label='Pencil Sale',color="Blue",width=0.3)
plt.bar(x_axis + 0.2 ,pen,label='Pen Sale',color="Gray",width=0.3)

plt.xticks(x_axis,year)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Stationery')
plt.legend()
plt.show()
"""

# Display employee id on x-axis and thier salaries on y-axis in the form of the a bargraoh for two departments
# import matplotlib.pyplot as plt
# x = [101,102,99,110,125]
# y = [25000,45000,12000,55000,38000]

# x1 = []
# x2 = []

# Pie Chart [represent the 100%]
# Display the data the sales of four different products of the company in the form of pie chart.
'''import matplotlib.pyplot as plt
#Taking the percentage of sales of the different products

sales_per = [35,10,25,30]
#Taking the names of the products
product_names = ['Hatch Back','Sedan','Premium','Commercial']
#Giving color to each product category
col = ['violet','Blue','Yellow','Gray']
#creating the pie chart using pie()
plt.pie(sales_per,labels=product_names,colors=col)
plt.title('Maruti Suzuki')
plt.legend()
plt.show()
'''

# 3D Pie Chart
'''from pygooglechart import PieChart3D
chart = PieChart3D(250,250)
chart.add_data([120,30,50,50,250])
chart.set_pie_labels('MCA BCA BBA MBA BCOM'.split())
chart.download('chart.png')'''


# students in 5 different programs
# import matplotlib.pyplot as plt
# students = [120,30,50,50,250]
# programs = ['MCA','MBA','BCA','BBA','BCOM']
# col = ['Blue','Yellow','Gray','Violet','Green']
# per = []

# plt.pie(students,labels=programs,colors=col)
# plt.title('Students')
# plt.legend()
# plt.show()


# LineGraph
# To draw a line chart to represent population increase in last five years
'''
import matplotlib.pyplot as plt
years = ['2023','2022','2021','2020','2019']
incr_pop = [70,45,29,35,75]
incr_pop1 = [10,40,30,20,60]
#Creating a line graph using plot()
plt.plot(years,incr_pop,color='Blue')
plt.plot(years,incr_pop1,color='Black')
plt.title('Population growth of India')
plt.xlabel('Years')
plt.ylabel('Increased_Of_Population_in_lacs')
plt.show()
'''

# Date 10-04-2024

# Scatter diagram
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(10)
print(x)
y = np.random.randn(10)
plt.scatter(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Diagram')
plt.show()
'''
# Area Plot
''' 
import numpy as np
import matplotlib.pyplot as plt
x = range(1,9)
y = [5,9,2,7,1,6,4,3]
plt.fill_between(x,y,color="black")
plt.title('Area Plot')
plt.show()
'''
