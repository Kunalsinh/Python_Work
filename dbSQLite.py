# Database Connectivity of SQLite in python

# Creating Database
import sqlite3
connection = sqlite3.connect('pydb.dp')

# Creating the table

connection.execute('CREATE TABLE student(rollno int, name varchar)')
print('Table created!')

# Inserting the records

connection.execute(
    """
INSERT INTO student VALUES
(1,'Rohit'),
(2,'Mahendra'),
(3,'Virat')
    """
)
print('Records inserted successfully!')
connection.commit()

# Retrieving the records from the table

cursor = connection.execute('SELECT * FROM student')
for i in cursor:
    print(i)

# Updating the records

update_query = """
UPDATE student SET name='Ravindra' WHERE rollno=1
"""
connection.execute(update_query)
print('Records Updated successfully!')

cursor = connection.execute('SELECT * FROM student')
for i in cursor:
    print(i)

# Deleting the records

delete_query = """
    DELETE FROM student WHERE rollno=1
"""
connection.execute(delete_query)
print('Records Deleted!')
cursor = connection.execute('SELECT * FROM student')
for i in cursor:
    print(i)
