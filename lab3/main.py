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

    def __init__(self):
        self.accounts = gen_users()

    def get_accounts(self):
        return self.accounts

    def add_account(self, account):
        self.accounts.append(account)





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


class CLIUserStub(CLIUserInput):
    def begin_user_interaction(self):
        self.login = 'l'
        self.password = 'p'
        self.resource = 'r'




class Authentication:
    account: Account
    us_username: str
    us_password: str

    def __init__(self):
        self.us_username = interface.login
        self.us_password = interface.password

    def login_check(self, db):
        if self.us_username == account.username:
            print(account.username)
            a.password_check(db)
        else:
            print("Не правильный логин или пароль")

    def password_check(self, db):

        if self.us_password == account.password:
            print("Аутефикация прошла успешно")
        else:
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
            # TODO: again login (Anton)

###################################################################
#interface = CLIUserStub()
db = Database()
interfaceU = CLIUserInput()

for account in db.get_accounts():
    print(account.username, account.password)


#interface.begin_user_interaction()
interfaceU.begin_user_interaction()
a = Authentication()
a.login_check(db)



# a


# user1 = Account(username='user1', password='user', groups=[groupadmin])
# db = Database()
# db.get_accounts()
# db.add_account(user1)
# for u in db.accounts:
#   print(u.username)
#  print(u.password)
