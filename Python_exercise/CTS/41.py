import json

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} - {self.salary}"

employees = {
    "emp1": Employee("Srishti", 50000),
    "emp2": Employee("Rahul", 60000)
}

data = {}

for key, emp in employees.items():
    data[key] = {
        "name": emp.name,
        "salary": emp.salary
    }

print("Employee Data Saved")

for key, value in data.items():
    print(value["name"], value["salary"])