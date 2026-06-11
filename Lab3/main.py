import mysql.connector

hussein_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hussein",
    database="hussein_company"
)

cursor = hussein_db.cursor()

class Employee : 
    employee_List = []

    def __init__(self, First_name, Last_name, Age,Department,Salary,type):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Age = Age
        self.Department = Department
        self.Salary = Salary
        self.type = type
        
        Employee.employee_List.append(self)
        
        sql = '''
        INSERT INTO employee (First_name, Last_name, Age,Department,Salary,type) VALUES (%s,%s,%s,%s,%s,%s)'''
        val = (self.First_name, self.Last_name, self.Age, self.Department, self.Salary, self.type)
        cursor.execute(sql,val)
        hussein_db.commit()
        
    def transfer(self,new_department):
        self.Department = new_department # update in Ram in code 
        sql = '''UPDATE employee SET Department = %s WHERE First_name = %s and Last_name = %s''' # update in DB
        val = (new_department, self.First_name, self.Last_name)
        cursor.execute(sql,val)
        hussein_db.commit()
            
    def fire(self):
        sql = "DELETE FROM employee WHERE first_name=%s AND last_name=%s"
        val = (self.First_name, self.Last_name)

        cursor.execute(sql, val)
        hussein_db.commit()

    def show(self):
        print(f''' Name : {self.First_name} {self.Last_name}
        Age : {self.Age}
        Department : {self.Department}
        Salary : {self.Salary}
        type : {self.type}''')
            
    @staticmethod
    def show_all_employees():
        cursor.execute("SELECT * FROM employee")
        employees = cursor.fetchall()
        for employee in employees:
            print(employee)
                
                
class Manager(Employee):
    def __init__(self, First_name, Last_name, Age,Department,Salary,managed_department):
        super().__init__(First_name, Last_name, Age,Department,Salary,"manager")
        self.managed_department = managed_department
        
        sql = "UPDATE employee SET managed_department = %s, type = %s WHERE First_name = %s and Last_name = %s"
        val = (self.managed_department, "manager", self.First_name, self.Last_name)
        cursor.execute(sql,val)
        hussein_db.commit()
        
    def show(self):
        print(f''' Name : {self.First_name} {self.Last_name}
        Age : {self.Age}
        Department : {self.Department}
        Salary : CONFIDENTIAL
        Managed Department : {self.managed_department}
        ''')





while True:
    print("\n===== Employee System =====")
    print("1. Add Employee")
    print("2. Add Manager")
    print("3. Transfer Employee")
    print("4. Fire Employee")
    print("5. Show All Employees")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = int(input("Age: "))
        department = input("Department: ")
        salary = float(input("Salary: "))
        type = "employee"

        Employee(first_name, last_name, age, department, salary, type)
        print("Employee Added Successfully")

    elif choice == "2":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = int(input("Age: "))
        department = input("Department: ")
        salary = float(input("Salary: "))
        managed_department = input("Managed Department: ")

        Manager(
            first_name,
            last_name,
            age,
            department,
            salary,
            managed_department
        )
        print("Manager Added Successfully")

    elif choice == "3":
        first_name = input("Employee First Name: ")
        last_name = input("Employee Last Name: ")
        new_department = input("New Department: ")

        for emp in Employee.employee_List:
            if emp.First_name == first_name and emp.Last_name == last_name:
                emp.transfer(new_department)
                print("Department Updated")
                break

    elif choice == "4":
        first_name = input("Employee First Name: ")
        last_name = input("Employee Last Name: ")

        for emp in Employee.employee_List:
            if emp.First_name == first_name and emp.Last_name == last_name:
                emp.fire()
                print("Employee Fired")
                break

    elif choice == "5":
        Employee.show_all_employees()

    elif choice == "6":
        print("Good Bye")
        break

    else:
        print("Invalid Choice")