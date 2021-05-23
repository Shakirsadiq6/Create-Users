'''Gender Validation'''

__author__ = "Shakir Sadiq"

class users_gender:
    '''class for users gender'''
    def __init__(self,sex):
        '''constructor'''
        self.sex = sex
sex = input("Enter your gender(M/F)? ")
while True:
    if sex in ('M','m','F','f'):
        break
    else:
        print("Enter a specific gender.")
        sex = input("Enter your gender again(M/F)? ")
sex_of_users = users_gender(sex)
sex_of_users.sex