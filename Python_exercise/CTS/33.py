def update_employee():
    emp1 = {"name": "Srishti", "salary": 50000}
    emp2 = {"department": "IT", "location": "Chennai"}

    emp1.update(emp2)

    print(emp1)

update_employee()