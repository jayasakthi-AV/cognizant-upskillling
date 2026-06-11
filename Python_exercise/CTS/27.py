def string_length(text):
    if text.strip() == "":
        return "Invalid string"

    return len(text)

text = "Python"

print("Length:", string_length(text))