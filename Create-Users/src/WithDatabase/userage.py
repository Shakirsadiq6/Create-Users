'''Age Validation'''

__author__ = "Shakir Sadiq"

class users_age:
    '''class for users age'''
    def __init__(self,age):
        '''constructor'''
        self.age = age
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Age must be a number.")
age_of_users = users_age(age)
age_of_users.age
