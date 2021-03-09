'''Email Validation'''

class users_email:
    '''class for users email'''
    def __init__(self,email):
        '''constructor'''
        self.email = email
email = input("Enter your email address: ")
while "@" not in email:
    print("Your email address must have '@' in it")
    email = input("Please write your email address again: ")
while "." not in email:
    print("Your email address must have '.' in it")
    email = input("Please write your email address again: ")
email_of_users = users_email(email)
email_of_users.email
