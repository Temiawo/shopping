# Adding employee
def Add_Employee():
    Rec = []
    while True:
        First_name = input("Enter Employee First Name : ")
        Last_name = input("Enter Employee Last Name : ")
        DOE = input("Enter Employee date of employment: ")
        Employee_id = input("Enter Employee Id: ")
        Salary = input("Enter Employee Salary : ")
        Department = input("Enter Employee Department: ")
        R=[First_name,Last_name,DOE,Employee_id,Salary,Department]
        Rec.append(R)
        print(Rec)
        ch=input("more records : (Y)/(N) ")
        if ch=='n' or ch== 'N' :
            print(Rec)
            menu();

def menu():
    print("welcome to Employee Management System")
    print("press ")
    print("1 to  Add New Employee")
    print("2 to Update Employee Information")
    print("3 to Remove Employees")
    print("4 to List Employee Information")
    print("5 to Exit")
    
    # Taking choice from user
    ch = int (input("Enter your choice "))
    if ch == 1:
        Add_Employee()
        
    elif ch == 2:
        Update_Employee()
            
    elif ch == 3:
        Remove_Employee()
        
    elif ch == 4:
        List_Employee()
        
    elif ch == 5:
        exit(0)
        
    else: 
        print ("invalid Choice")
        menu()

#calling menu function
menu() 


            
    