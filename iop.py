# import mysql.connector
# from mysql.connector import Error

# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='manthan',
#                                          user='root',
#                                          password='')
#     mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
#                              Id int(11) NOT NULL,
#                              Name varchar(250) NOT NULL,
#                              Price float NOT NULL,
#                              Purchase_date Date NOT NULL,
#                              PRIMARY KEY (Id)) """
#     sql = """INSERT INTO Laptop(
#    Id,Name, Price, Purchase_date)
#    VALUES ('1','Mac', '1500', 08/09/2020)"""

#     cursor = connection.cursor()
#     result = cursor.execute(mySql_Create_Table_Query, sql)
#     print("Laptop Table created successfully ")

# except mysql.connector.Error as error:
#     print("Failed to create table in MySQL: {}".format(error))
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='password', host='127.0.0.1', database='mydb')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
   # Executing the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

# Closing the connection
conn.close()