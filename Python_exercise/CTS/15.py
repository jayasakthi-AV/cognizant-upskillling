def validate_login(user, pwd):
    if user.strip() == "" or pwd.strip() == "":
        return "Username or Password cannot be empty"

    if user == "admin":
        if pwd == "pass123":
            return "Login Successful"
        else:
            return "Incorrect Password"
    else:
        return "Invalid Username"

user = "admin"
pwd = "pass123"

print(validate_login(user, pwd))