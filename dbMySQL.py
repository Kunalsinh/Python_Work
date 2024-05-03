import mysql.connector
import sys

myConnection = mysql.connector.connect(
    host='localhost', user='root', password='', database='mypy')
mycursor = myConnection.cursor()


def crudMenu():
    print("CRUD MENU LIST")
    print("1.Create Database.")
    print("2.Create Table.")
    print("3.Insert Records.")
    print("4.Show   Records.")
    print("5.Update Records.")
    print("6.Delete Records.")
    print("7.Exit")


def createDatabse():
    create_database = 'CREATE DATABASE mypy'
    mycursor.execute(create_database)
    print('Database created successfully.')


def createTable():
    create_table = 'CREATE TABLE student(rollno int,name varchar(50))'
    mycursor.execute(create_table)
    print('Table created succesfully.')


def insertRecords():
    insert_query = 'INSERT INTO student (rollno,name) VALUES (%s,%s)'
    records = [(1, 'Virat'), (2, 'Mahi'), (3, 'Rohit'), (4, 'Ravindra')]
    mycursor.executemany(insert_query, records)
    myConnection.commit()
    print('Records inserted successfully!')


def showRecords():
    show_record = 'SELECT * FROM student'
    mycursor.execute(show_record)
    result = mycursor.fetchall()
    for i in result:
        print(i)


def updateRecords():
    update_query = "UPDATE student SET name='Rachindra' WHERE rollno=4"
    mycursor.execute(update_query)
    myConnection.commit()
    print('Record updated successsfully!')


def deleteRecords():
    delete_query = 'DELETE FROM student WHERE rollno=4'
    mycursor.execute(delete_query)
    myConnection.commit()
    print('Record deleted successfully!')


def userChoice():
    choice = int(
        input("Enter appropriate number from menu to do your work : "))
    if choice == 1:
        createDatabse()
    if choice == 2:
        createTable()
    if choice == 3:
        insertRecords()
    if choice == 4:
        showRecords()
    if choice == 5:
        updateRecords()
    if choice == 6:
        deleteRecords()
    if choice == 7:
        print("Exited!")
        sys.exit()


while True:
    crudMenu()
    userChoice()
