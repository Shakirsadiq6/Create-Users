'''Name Validation'''

class users_name:
    '''class for users name'''
    def __init__(self, name):
        '''constructor'''
        self.name = name
name = input("Enter name: ")
while name.isdigit() or name == '' or name.isspace():
    print("Name cannot be blank or have digits.")
    name = input("Please enter only alphabetical characters for name: ")
names_of_users = users_name(name)
names_of_users.name
