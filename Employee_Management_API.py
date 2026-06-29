import requests

base_url="https://jsonplaceholder.typicode.com/users"

while True:
    print("===== Employee Management =====")
    print("1. View Employee")
    print("2. Add Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if (choice==1):
            emp_id=int(input("enter employee id="))
            url=f"{base_url}/{emp_id}"
            response=requests.get(url)
            if (response.status_code==200):
                emp=response.json()
                print("Name=",emp["name"])
                print("Email=",emp["email"])
                print("Company=",emp["company"]["name"])
            elif(response.status_code==404):
                print("Employee not found")
            else:
                print(response.status_code,"Error occurred")


        elif(choice==2):
            name=input("enter employee name=")
            salary=int(input("enter salary of employee="))
            employee={
                "name":name,
                "salary":salary
            }
            response=requests.post(base_url,json=employee)
            if(response.status_code==201):  
                emp=response.json()
                print("employee added successfully")
                print("id :",emp["id"])
                print("Name :", emp["name"])
                print("Salary :", emp["salary"])  
            else:
                print(response.status_code,"error occurred")


        elif(choice==3):
            emp_id=int(input("enter employee id="))
            salary=int(input("enter updated salary="))
            employee={
                "salary":salary
            }
            url=f"{base_url}/{emp_id}"
            response=requests.put(url,json=employee)
            if(response.status_code==200):
                print("user updated succesfully")
                emp=response.json()
                print("Salary :",emp["salary"])
            elif(response.status_code==404):
                print("employee not found")
            else:
                print(response.status_code,"error occurred")

        elif(choice==4):
            emp_id=int(input("enter employee id="))
            url=f"{base_url}/{emp_id}"
            response=requests.delete(url)
            if(response.status_code==200):
                print("user deleted successfully")
            elif(response.status_code==404):
                print("user  ot found")
            else:
                print(response.status_code,"error occurred")

        elif(choice==5):
            break
        
        else:
            print("Invalid choice")

    except ValueError:
        print("please enter the valid number")   