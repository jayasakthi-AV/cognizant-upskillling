employees = [
    {"name": "Srishti", "salary": 60000},
    {"name": "Rahul", "salary": 45000},
    {"name": "Anu", "salary": 70000}
]

high_salary = [emp for emp in employees if emp["salary"] > 50000]

average = sum(emp["salary"] for emp in employees) / len(employees)

print("Employees with salary > 50000:")
print(high_salary)

print("Average Salary:", average)