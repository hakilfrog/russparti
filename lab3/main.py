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
    us_username = interface.login
    us_password = interface.password
    #def __init__(self, us_username, us_password):
       ##us_password = us_password

    def login_check(self, db, interface):

        for account in db.accounts:
            if interface.login == account.username:
                print("А ты хорош")
            else:
                print("хуесос")



           # try: interface.login
           # except AuthentificationError:
               # print('ERROR #1')



    def proverka(self, db):
        for account in db.accounts:
           print(account.username)
                    #TODO: again login (Anton)











db.get_accounts()
da=CLIUserInput()
da.begin_user_interaction()
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




