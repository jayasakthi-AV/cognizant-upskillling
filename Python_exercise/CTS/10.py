def next_year_age():
    age = input("Enter your age: ")

    if age.isdigit():
        age = int(age)
        print(f"Next year you'll be {age + 1}")
    else:
        print("Invalid age")

next_year_age()