''' create a script that will create multiple users by taking
their details as input and keeping the constraints in consideration'''

__author__ = "Shakir Sadiq"

username_list = []
for users in range(1,6):
    name = input("Enter name:")
    while name.isdigit() or name == '' or name.isspace():
        print("Name cannot be blank or have digits.")
        name = input("Please enter only alphabetical characters for name: ")
    age = int(input("Enter your age: "))
    sex = input("Enter your gender(M/F)? ")
    username = input("Enter a username: ")
    username_list.append(username)
    if len(username_list) != len(set(username_list)):
        print("Username already taken!")
        break
    email = input("Enter your email address: ")
    while "@" not in email:
        print("Your email address must have '@' in it")
        email = input("Please write your email address again: ")
    while "." not in email:
        print("Your email address must have '.' in it")
        email = input("Please write your email address again: ")
    CAPITAL = 0
    SMALL = 0
    DIGITS = 0
    SPECIAL_CHARACTERS = 0
    password = input("Enter your password: ")
    while True:
        if (len(password)>=8):
            for i in password:
                if (i.isupper()):
                    CAPITAL += 1
                if (i.islower()):
                    SMALL += 1
                if (i.isdigit()):
                    DIGITS += 1
                if i in ['!','@','#','$','%','^','&','*','.']:
                    SPECIAL_CHARACTERS += 1
        if (CAPITAL>=1 and SMALL>=1 and DIGITS>=1 and SPECIAL_CHARACTERS>=1 and CAPITAL+SMALL+DIGITS+SPECIAL_CHARACTERS==len(password)):
            break
        else:
            print("password must be at least 8 characters long contain at least 1 uppercase, 1 lowercase, 1 special character and 1 digit.")
            password = input("Enter your password: ")
    print()
    print("Details of User",users,":")
    print("Name:", name)
    print("Age:", age)
    print("Gender:", sex)
    print("Username:", username)
    print("Email:", email)
    print("Password:", password)
    print()
