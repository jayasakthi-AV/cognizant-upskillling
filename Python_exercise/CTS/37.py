class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee Name:", self.name)

emp1 = Employee("Srishti")
emp2 = Employee("Dhanush")

emp1.display()
emp2.display()