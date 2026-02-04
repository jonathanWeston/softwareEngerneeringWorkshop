# Write a script that:
# • Asks the user to enter a password.
# • Checks if the entered password contains at least 10 characters, at least one number
# and a mix of upper and lowercase letters.
# o If the password is invalid, report an error to the user and re-ask for a
# password.
# • Ask the user to confirm the password by re-entering it.
# • Check if the passwords match.
# o If the passwords match, display "success”.
# o If the passwords do not match, display “unsuccessful: passwords do not
# match” and ask the user to try again.

def password_checker():
    password = input("please enter the password that you want to use ")
    number_check = False
    upper_check = False
    lower_check = False
    if len(password) >= 10:
        for char in password:
            if char.isdigit():
                number_check = True
            elif char.isupper():
                upper_check  = True
            elif char.islower():
                lower_check = True
    else:
        print("password invalid, your password needs to be longer")
        return password_checker()
    if upper_check and lower_check and number_check:
        print("password valid")
        return password
    else:
        print("password invalid")
        return password_checker()

def password_matcher(password):
    password_check = input("Reenter your password")
    if password == password_check:
        print("success")
    else:
        print("password was not a match ")
        try_again = input("do you want to try again? yes/no ")
        if (try_again == "yes"):
            return password_matcher(password)
        else:
            print("your password has not changed ")
            exit()

password = password_checker()
password_matcher(password)
