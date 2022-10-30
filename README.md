# Bootcamp-Project-1-Python

## Employee Record System

Employee Record System is software built to handle the primary housekeeping functions of a company. ERS helps companies keep track of all the employees and their records. It is used to manage the company using a computerized system. This software built to handle the records of employees of any company. It will help companies to keep track of all the employees’ records in a file.

Aim of the Employee’s Record System: The user will be provided with 6 options:

Add a new record.
Delete a record.
Modify a record.
View all the records.
Number of employees
Exit.

Data of the Employees:
Name.
Age.
Salary.
Employee ID.

-------------------------------------------------------


def addRecord(recordsDic):
    i = True
    while i == True:
        name = input("Enter name: ")
        age = input("Enter age: ")
        salary = input("Enter salary: ")
        EMP_ID = input("Enter EMP-ID: ")
        
        recordsDic[name] = {
            "Name": name,
            "Age": age,
            "Salary": salary,
            "ID": EMP_ID
        }
        
        print(recordsDic)
        
        anotherRecord = input("Want to add another record (y/n) : ")
        if (anotherRecord == 'y'):
            continue
        elif (anotherRecord == 'n'):
            break
        else:
            print("Your choice is wrong try again..")
    return recordsDic

def displyRecords(recordlist):
    print("=====================================")
    print("NAME \t  AGE \t  SALARY\tID")
    
    print("=====================================")
    for p_id, p_info, in recordlist.items():
        for key in p_info:   print(p_info[key],end="\t  ")
        print("\n")
    

def modifyRecords(recordlist):
    oldName = input("Enter employee name to modify: ")
    newName = input("Enter new name: ")
    newAge = input("Enter new age: ")
    newSalary = input("Enter new salary: ")
    newID = input("Enter new EMP-ID: ")
    recordlist[oldName] = {"Name": newName,"Age": newAge,"Salary": newSalary,"ID": newID}
    displyRecords(recordlist)

def deleteRecords(recordlist):
    delName = input("Enter employee name to delete: ")
    del recordlist[delName]
    displyRecords(recordlist)
        
i = True
count1 = 0
count2 = 0
lst = {}
while i == True:
    print("\n*********####### EMPLOYEE RECORD #######*********")
    print("1. Add record")
    print("2. Display records")
    print("3. Modify record")
    print("4. Delete record")
    print("5. Number of employees")
    print("6. Exit")
    
    userInput = input("Enter one of the above : ")
    if(userInput == '1'):
        lst = addRecord(lst)
        count2 = count2 + 1
    elif(userInput == '2'):
        displyRecords(lst)
    elif(userInput == '3'):
        modifyRecords(lst)
    elif(userInput == '4'):
        deleteRecords(lst)
        count1 = count1 + 1
    elif(userInput == '5'):
        sum = lambda x, y : y - x
        print(sum(count1, count2))
    continue

