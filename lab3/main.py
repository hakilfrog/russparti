# AAA
import random


class Group:
    name = ''
    rights = list()

    def __init__(self, name, rights):
        self.name = name
        self.rights = rights


class Account:
    username = ''
    password = ''
    groups: list[Group] = list()

    def __init__(self, username, password, groups):
        self.username = username
        self.password = password
        self.groups = groups


groupadmin = Group(name='groupadmin', rights=['p', 's'])


def gen_users():
    users = list()
    for user in range(20):
        user = Account(username='u_' + str(random.randint(10, 99)), password='p_' + str(random.randint(100, 999)),
                       groups=[groupadmin])
        users.append(user)
    return users


class Database:

    accounts: list[Account] = list()
    groups: list[Group] = list()

    def get_accounts(self):
        self.accounts = gen_users()
        return self.accounts

    def add_account(self, account):
        self.accounts.append(account)


db = Database()

class AuthentificationError(Exception):
    pass


class AuthorizationError(Exception):
    pass
class CLIUserInput:
    login: str
    password: str
    resource: str

    def begin_user_interaction(self):
        self.login = input("Введите логин")
        self.password = input("Введите пароль")
        self.resource = input("Введите ресурс к которому хотет доступ")
        return self.login, self.password, self.resource


interface = CLIUserInput()


class Authentication:
    account: Account
    us_username: str
    us_password: str
    def __init__(self, ):
       self.us_username = interface.login
       self.us_password = interface.password


    def login_check(self, db):
        count = 0
        for account in db.accounts:
            count += 1
            if self.us_username == account.username:
                somechel.password_check(db)
                break
            elif count == len(db.accounts):
                print("Не правильный логин или пароль")

    def password_check(self, db):
        count = 0
        for account in db.accounts:
            count += 1
            if self.us_password == account.password:
                print("Аутефикация прошла успешно")
                break
            elif count == len(db.accounts):
                print("Не правильный логин или пароль1")












           # try: interface.login
           # except AuthentificationError:
               # print('ERROR #1')

    #         try:
    #             self.login_check(db)
    #         except AuthentificationError:
    #              print('ERROR #1')



    def proverka(self, db):
        for account in db.accounts:
           print(account.username)
                    #TODO: again login (Anton)











db.get_accounts()
for account in db.accounts:
    print(account.username)
    print(account.password)
interface.begin_user_interaction()
somechel = Authentication()
somechel.login_check(db)












#a






#user1 = Account(username='user1', password='user', groups=[groupadmin])
#db = Database()
#db.get_accounts()
#db.add_account(user1)
#for u in db.accounts:
 #   print(u.username)
  #  print(u.password)




