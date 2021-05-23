''' create a script that will create multiple users by taking
their details as input and keeping the constraints in consideration'''

__author__ = "Shakir Sadiq"

username_list = []
def name_function():
    ''' function for users name'''
    return name
    
def age_function():
    '''fucntion for users age'''
    return age

def gender():
    '''function for users gender'''
    return sex

def username_function():
    '''function for a unique username'''
    return username

def email_function():
    '''function for users email'''
    return email

def password_function(password):
    '''function used to validate the password'''
    special_characters =['!','@','#','$','%','^','&','*','.']
    value = True
    if len(password) < 8:
        value = False
    if not any(i.isdigit() for i in password):
        value = False
    if not any(i.isupper() for i in password):
        value = False
    if not any(i.islower() for i in password):
        value = False
    if not any(i in special_characters for i in password):
        value = False
    if value:
        return value
def main():
    '''main function'''
    for users in range(1,6):
        name = input("Enter name:")
        while name.isdigit() or name == '' or name.isspace():
            print("Name cannot be blank or have digits.")
            name = input("Please enter only alphabetical characters for name: ")

        while True:
            try:
                age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Age must be a number.")

        sex = input("Enter your gender(M/F)? ")
        while True:
            if sex in ('M','m','F','f'):
                break
            else:
                print("Enter a specific gender.")
                sex = input("Enter your gender again(M/F)? ")

        while len(username_list) == len(set(username_list)):
            username = input("Enter a username:")
            if username not in username_list:
                username_list.append(username)
                break
            else:
                print("Username already taken! Try again!")

        email = input("Enter your email address: ")
        while "@" not in email:
            print("Your email address must have '@' in it")
            email = input("Please write your email address again: ")
        while "." not in email:
            print("Your email address must have '.' in it")
            email = input("Please write your email address again: ")

        while True:
            password = input("Enter your password: ")
            if password_function(password):
                break
            else:
                print("Password must be at least 8 characters long, ",end="")
                print("it should contain at least 1 uppercase, ",end="")
                print("1 lowercase, 1 special character and 1 digit.")

        print()
        print("Details of User",users,":")
        print("Name:", name)
        print("Age:", age)
        print("Gender:", sex)
        print("Username:", username)
        print("Email:", email)
        print("Password:", password)
        print()
main()
