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



class Authentication:
    account: Account
    us_username: str
    us_password: str

    def __init__(self, us_username, us_password):
        us_username = us_username
        us_password = us_password

    def proverka(self,db):
        for account in db.accounts():
            if self.us_username == account.username:
                if self.us_password == account.password:
                    print("все заебок")
                else:
                    print("Неправильный пароль")
                    #TODO: again login (Anton)












somechel = Authentication(us_username='a', us_password='p')
















user1 = Account(username='user1', password='user', groups=[groupadmin])
db = Database()
db.get_accounts()
db.add_account(user1)
for u in db.accounts:
    print(u.username)
    print(u.password)




