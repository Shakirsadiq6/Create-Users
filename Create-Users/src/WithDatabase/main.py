'''Database queries to handle all the user input details in the database'''

__author__ = "Shakir Sadiq"

import psycopg2
import names
import userage
import gender
import emails
import usernames
import password

class database:
    '''class for database connections and queries'''
    def __init__(self, dbname, user, password):
        '''constructor for db connection'''
        self.db = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
        self.cursor = self.db.cursor()
    def fetchall(self, sql):
        '''fucntion for fetch data'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def execute(self, query, data=None):
        '''function for execute commands'''
        self.cursor.execute(query, data)
        self.db.commit()
    def close(self):
        '''function for closing db connection'''
        self.cursor.close()
try:
    connect_db = database("Users", "postgres", "shakir789")
    query = "create table createuser(Name varchar, Age varchar, Gender varchar, Email varchar unique, Username varchar unique, Password varchar)"
    connect_db.execute(query)
    query = "insert into createuser(Name, Age, Gender, Email, Username, Password) values(%s,%s,%s,%s,%s,%s)"
    connect_db.execute(query, (names.name, userage.age, gender.sex, emails.email, usernames.username, password.password))
    result = connect_db.fetchall("select * from createuser")
    for i in result:
        print("\nName:", i[0], "\nAge:", i[1], "\nGender:", i[2], "\nEmail: ", i[3], "\nUsername:", i[4], "\nPassword:", i[5])
except psycopg2.errors.DuplicateTable:
    try:
        connect_db = database("Users", "postgres", "shakir789")
        query = "insert into createuser(Name, Age, Gender, Email, Username, Password) values(%s,%s,%s,%s,%s,%s)"
        connect_db.execute(query, (names.name, userage.age, gender.sex, emails.email, usernames.username, password.password))
        result = connect_db.fetchall("select * from createuser")
        for i in result:
            print("\nName:", i[0], "\nAge:", i[1], "\nGender:", i[2], "\nEmail: ", i[3], "\nUsername:", i[4], "\nPassword:", i[5])
    except psycopg2.errors.DuplicateTable:
        print("Values already exist in the table!")
    except psycopg2.errors.UniqueViolation:
        print("\nYou have entered the duplicate Email ID or Username!")
        print("Please enter unique Email ID and Username!")
finally:
    connect_db.close()
    print("\nDatabase server connection is closed!")
