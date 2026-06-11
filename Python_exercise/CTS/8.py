def salary_details(salaries):
    if len(salaries) == 0:
        return "Invalid salary list"
    
    minimum = min(salaries)
    maximum = max(salaries)

    return f"Lowest Salary: {minimum}\nHighest Salary: {maximum}"

salary_list = [50000, 75000, 62000, 95000]

print(salary_details(salary_list))