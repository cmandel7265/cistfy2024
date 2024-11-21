employee_data1 = open("Employees.dat", "a")
last_Name = input("Please input your last name. ")
employee_data2 = open("Employees.dat", "w")
employee_data2.write(last_Name)
first_Name = input("Please input your first name. ")
employee_data3 = open("Employees.dat", "w")
employee_data3.write(first_Name)
employee_ID = input("Please input ID number. ")
if employee_ID !=  RE49762358 or PR156125 or OF45461 or RE68566547 or PR156984:
    employee_ID = input("Please input ID number again. ")
else:
    employee_data4 = open("Employees.dat", "w")
    employee_data4.write(employee_ID)
employee_Wage = input("Please write employee wage. ")
employee_Wage = float(employee_Wage)
if employee_Wage == 0 or >= 45.50:
    employee_Wage = input("Please write employee wage again. ")
else:
    employee_data5 = open("Employee.dat", "w")
    employee_data5.write(employee_Wage)
employee_data1.close()