import mysql.connector

#establishing the connection
connection = mysql.connector.connect(host='localhost',
                                         database='manthan',
                                         user='root',
                                         password='')

#Creating a cursor object using the cursor() method
cursor = connection.cursor()

# Preparing SQL query to INSERT a record into the database.
# insert_stmt = (
#    "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
#    "VALUES (%s, %s, %s, %s, %s)"
# )
# data = ('Ramya', 'Ramapriya', 25, 'F', 5000)
# data = ('manthan', 'kolhe', 22, 'M', 600)

# try:
#    # Executing the SQL command
#    cursor.execute(insert_stmt, data)
   
#    # Commit your changes in the database
#    connection.commit()

# except:
#    # Rolling back in case of error
#    connection.rollback()

# print("Data inserted")

# # Closing the connection
# connection.close()

sql = '''SELECT * from EMPLOYEE'''

#Executing the query
cursor.execute(sql)

#Fetching 1st row from the table
result = cursor.fetchmany(size =2);
print(result)

#Closing the connection
connection.close()