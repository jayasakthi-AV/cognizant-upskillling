def employee_salary():
    employees = {
        "IT": {
            "Rahul": 50000,
            "Anu": 60000
        },
        "HR": {
            "Kiran": 45000
        }
    }

    department = "IT"
    employee = "Anu"

    if department in employees:
        if employee in employees[department]:
            print("Salary:", employees[department][employee])
        else:
            print("Employee not found")
    else:
        print("Department not found")

employee_salary()