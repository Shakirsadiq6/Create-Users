'''Password Validation'''

__author__ = "Shakir Sadiq"

import re
class users_password:
    '''class for users password'''
    def __init__(self,password):
        '''constructor'''
        self.password = password
while True:
    #regex pattern for password validation.
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&+=]).*$"
    #^ = start of input.
    #(?=.{8,}) =  Make sure password be at least 8 characters long.
    #(?=.*\d) = Make sure there is at least one digit.
    #(?=.*?[a-z]) = Make sure there is at least one lower case letter.
    #(?=.*?[A-Z]) = Make sure there is at least one upper case letter.
    #(?=.*[@#$%^&+=]) = Make sure there is at least one special character.
    #$ = end of input.
    password = input("Enter your password: ")
    result = re.findall(pattern, password)
    if (result):
        break
    else:
        print("Password must be at least 8 characters long, ",end="")
        print("it should contain at least 1 uppercase, ",end="")
        print("1 lowercase, 1 special character and 1 digit.")
password_of_users = users_password(password)
password_of_users.password
