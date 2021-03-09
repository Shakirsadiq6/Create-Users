'''Username Validation'''

username_list = []
class users_username:
    '''class for users username'''
    def __init__(self,username):
        '''constructor'''
        self.username = username
username = input("Enter a username:")
username_of_users = users_username(username)
username_of_users.username
