def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Invalid input"

    return a + b

result = add(5, 3)

print("Sum:", result)