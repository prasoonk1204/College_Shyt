import sqlite3

try:
    connection = sqlite3.connect("myemp.db")
    print("Database has been created successfully...")
except Exception as e:
    print("Database creation failed...")
    print("Error message:", e)
    print("Error Type:", type(e))


sqlStr = '''
         CREATE TABLE employee (
             emp_id INTEGER PRIMARY KEY,
             emp_name TEXT,
             emp_city TEXT,
             emp_salary REAL
         );
         '''
try:
    connection.execute(sqlStr)
    print("Database table has been created successfully...")
except:
    print("Error !!! Error !!! Error !!!")


print(connection.execute("pragma table_info('employee')"))
print(list(connection.execute("pragma table_info('employee')")))  # list of tuple
print("Displaying the table structure...")
for my_tuple in list(connection.execute("pragma table_info('employee')")):
    print (my_tuple)


# inserting records in the database table reading content from the csv file
import csv
with open("emp_data.csv") as data_file:
    # reader to read the data file content and store them into a table
    csv_reader = csv.reader(data_file)
    # reader will read the data file content separated by the delimiter ,
    print(list(csv_reader))  # list of lists
    print(len(list(csv_reader)))


# inserting records in the database table reading content from the csv file
import csv
sqlStr = "INSERT INTO employee VALUES ('{ID_PH}','{Name_PH}','{City_PH}','{Salary_PH}');"
with open("emp_data.csv") as data_file:
    # reader to read the data file content and store them into a table
    csv_reader = csv.reader(data_file)
    # reader will read the data file content separated by the delimiter ,
    for row in list(csv_reader):
        connection.execute(sqlStr.format(ID_PH=row[0], Name_PH=row[1], City_PH=row[2], Salary_PH=row[3]))
    print("All records got successfully inserted...")
print("End of the INSERT operation...")


# to make the change permanent
connection.commit()


# retrieving table records using select queries
# SQl for fetching all records from the database table
sqlStr = "SELECT * FROM employee;"
# read records from the database table and put them in a cursor
cur_table = connection.execute(sqlStr)
# print(cur_table)
# print(list(cur_table))
print("Displaying all the records for the database table:")
for row in cur_table:
    print(f"Emp-ID: {row[0]}, Emp-Name: {row[1]}, Emp-City: {row[2]} and Emp-Salary: {row[3]}...")
print("End of display of records...")


# update operation on the database table
# update salary to 30,000 where city is 'Chennai'
sqlStr = "UPDATE employee SET emp_salary = 30000 WHERE emp_city = 'Chennai';"
table = connection.execute(sqlStr)
connection.commit()    # to make the change permanent
print("So the number of records updated is:", table.rowcount)
print("UPDATE operation has been completed successfully...")


# SQl for fetching all records from the database table
sqlStr = "SELECT * FROM employee;"
# read records from the database table and put them in a cursor
cur_table = connection.execute(sqlStr)
print("Displaying all the records for the database table:")
for row in cur_table:
    print(f"Emp-ID: {row[0]}, Emp-Name: {row[1]}, Emp-City: {row[2]} and Emp-Salary: {row[3]}...")
print("End of display of records...")


# assignment-1
# fetch employee name and salary of those employees whose salary >= 30000
sqlStr = "SELECT emp_name, emp_salary FROM employee WHERE emp_salary >= 30000;"
# read records from the database table and put them in a cursor
cur_table = connection.execute(sqlStr)
print("Displaying all the records for the database table:")
for row in cur_table:
    print(f"Emp-Name: {row[0]} and Emp-Salary: {row[1]}...")
print("End of display of records...")


# assignment-2
# fetch employee name, salary and 7.5% TDS against salaries of all employees
sqlStr = "SELECT emp_name, emp_salary, emp_salary * 0.075 FROM employee;"
# read records from the database table and put them in a cursor
cur_table = connection.execute(sqlStr)
print("Displaying all the records for the database table:")
for row in cur_table:
    print(f"Emp-Name: {row[0]}, Emp-Salary: {row[1]} and Emp-TDS: {row[2]}...")
print("End of display of records...")


# assignment-3
# display city wise average salaries from the employee table
sqlStr = "SELECT emp_city, AVG(emp_salary) FROM employee GROUP BY emp_city;"
# read records from the database table and put them in a cursor
cur_table = connection.execute(sqlStr)
print("Displaying all the records for the database table:")
for row in cur_table:
    print(f"Emp-City: {row[0]} and Emp-Salary_Average: {row[1]}...")
print("End of display of records...")


# deleting records from a table
# delete those records where emp_city = 'Kolkata'
sqlStr = "DELETE FROM employee WHERE emp_city = 'Kolkata';"
table = connection.execute(sqlStr)
connection.commit()    # to make the change permanent
print("So the number of records deleted is:", table.rowcount)
print("DELETE operation has been completed successfully...")


print("Displaying all the records for the database table:")
sqlStr = "SELECT * FROM employee;"
cur_table = connection.execute(sqlStr)
for row in cur_table:
    print(f"Emp-Name: {row[0]}, Emp-Salary: {row[1]} and Emp-TDS: {row[2]}...")
print("End of display of records...")


# take input from from the user on how many records to input in the table
n = int(input("Please enter the number of records to insert:"))
for i in range(n):
    ID = int(input("Please enter the employee ID:"))
    name = input("Please enter the employee name:")
    city = input("Please enter the employee city:")
    salary = float(input("Please enter the employee salary:"))
    sqlStr = "INSERT INTO employee VALUES ({}, '{}', '{}', {});".format(ID, name, city, salary)
    table = connection.execute(sqlStr)
    connection.commit()    # to make the change permanent
    print("So the number of records inserted is:", table.rowcount)
    print("INSERT operation has been completed successfully...")


print("Displaying all the records for the database table:")
sqlStr = "SELECT * FROM employee;"
cur_table = connection.execute(sqlStr)
for row in cur_table:
    print(f"Emp-Name: {row[0]}, Emp-Salary: {row[1]} and Emp-TDS: {row[2]}...")
print("End of display of records...")