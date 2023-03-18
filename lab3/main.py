import random
import datetime


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


def gen_users():
    users = list()
    for user in range(20):
        user = Account(username='u_' + str(random.randint(10, 99)), password='p_' + str(random.randint(100, 999)),
                       groups=[groupuser])
        users.append(user)
    return users


class Database:
    accounts: list[Account] = list()
    groups: list[Group] = list()

    def gen_users(self):
        self.accounts = gen_users()

    def get_accounts(self):
        return self.accounts

    def add_account(self, account):
        self.accounts.append(account)

    def add_group(self, group):
        self.groups.append(group)

    def output(self):
        for account in self.get_accounts():
            print(account.username, account.password, end=' ')
            for group in account.groups:
                print(group.name, end=' ')
            print()


class AuthentificationError(Exception):
    pass


class AuthorizationError(Exception):
    pass


class CLIUserInput:
    login: str
    password: str
    resource_request: str


    def begin_user_interaction(self, login, password):
        self.login = input("Введите логин")
        self.password = input("Введите пароль")
        #  self.resource = input("Введите ресурс к которому хотет доступ")

    def user_interaction(self, account, resource_request):
        self.resource_request =input("Чё надо, падла:")
        authorize.access_check(account, resource_request)


class CLIUserStub(CLIUserInput):

    def begin_user_interaction(self, login='l', password='p'):
        self.login = login
        self.password = password
        # a.login_check(testuser) !!! почему "а" не работает из метода, а "audit" работает???

    def user_interaction(self, account, resource_request='r'):
        self.resource_request = resource_request
        authorize.access_check(account, resource_request)


class Authentication:
    account: Account
    us_username: str
    us_password: str

    def __init__(self, interface):
        self.us_username = interface.login
        self.us_password = interface.password

    def login_check(self, account):
        if self.us_username == account.username:
            audit.add_incident(Incident(account, datetime.datetime.now(), status=True, action="login"))
            if self.us_password == account.password:
                print("Аутентификация прошла успешно")
                audit.add_incident(Incident(account, datetime.datetime.now(), status=True, action="password"))

            else:
                print("Неправильный логин или пароль")
                audit.add_incident(Incident(account, datetime.datetime.now(), status=False, action="password"))
        else:
            #  self.password_check(account)
            audit.add_incident(Incident(account, datetime.datetime.now(), status=False, action="login"))
            print("Неправильный логин или пароль")


class Authorization:

    def access_check(self, account, resource_request):
        for group in account.groups:
            if resource_request in group.rights:
                print("Доступ разрешён!")
            else:  # в каких-то хоть группах
                for db_group in db.groups:
                    if resource_request in db_group.rights:
                        print("У вас нет прав - вы женщина")
                    else:
                        print("Нет такого действия")


class Incident:
    user_account: Account
    time: datetime
    status: bool
    action: str

    def __init__(self, user_name, time, status, action):
        self.user_account = user_name
        self.time = time
        self.status = status
        self.action = action


class Audit:
    incidents: list[Incident] = list()

    def get_incidents(self):
        for incident in self.incidents:
            if incident.status:
                print(f'<------------------> {incident.time} | user: \'{incident.user_account.username}\' | action: '
                      f'{incident.action} | ip: 127.0.0.1 <----------------->')
            else:
                print(f'<####-ERROR-#######> {incident.time} | user: \'{incident.user_account.username}\' | action: '
                      f'{incident.action} | ip: 127.0.0.1 <#################>')

    def add_incident(self, incident):
        self.incidents.append(incident)


###################################################################
audit = Audit()
###
db = Database()
###
groupadmin = Group(name='groupadmin', rights=['kill', 'word'])
groupuser = Group(name='users', rights=['google', 'ya.oru'])
db.add_group(groupadmin)
db.add_group(groupuser)
###
db.gen_users()
###
interfaceU = CLIUserInput()
interfaceM = CLIUserStub()
###
testuser = Account('l', 'p', groups=[groupadmin, groupuser])
db.add_account(testuser)
someuser = Account('lol', 'p', groups=[])
db.add_account(someuser)
###
interfaceM.begin_user_interaction('l', 'p')
a = Authentication(interfaceM)
a.login_check(testuser)
###
authorize = Authorization()

###
audit.get_incidents()

#  db.output()
