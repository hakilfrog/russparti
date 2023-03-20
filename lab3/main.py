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


class NoAccount:
    login: str = ''
    password: str = ''
    int: int
    request: str

    def init(self, login, password, request):
        self.login = login
        self.password = password
        self.request = request
        self.int = 0  # интерфейс пользователя (1 - CLI, 0 - просто)

    def cli_itin(self):
        self.login = input('Введите логин')
        self.password = input('Введите пароль')
        self.int = 1


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
    resource_request: str = None

    def begin_user_interaction(self, some_noaccount):
        some_noaccount = NoAccount()
        some_noaccount.cli_itin()
        return some_noaccount

    def user_interaction(self, account, resource_request):
        self.resource_request = input("Чё надо, падла:")
        return resource_request


class CLIUserStub(CLIUserInput):

    def begin_user_interaction(self, login='l', password='p', request='kill'):
        some_noaccaunt = NoAccount()
        some_noaccaunt.init(login, password, request)
        return some_noaccaunt

    def user_interaction(self, account, resource_request=None):
        if resource_request is None:
            resource_request = input("Чё надо, падла:")
        self.resource_request = resource_request
        return account, resource_request


class Authentication:
    noaccount: NoAccount
    us_username: str
    us_password: str
    statusl = True
    statusp = True

    def __init__(self, noaccount):
        self.noaccount = noaccount

    def credentials_check(self, database):
        try:
            for account in database.accounts:
                if self.noaccount.login == account.username:
                    self.statusl = True

                    if self.noaccount.password == account.password:
                        self.statusp = True
                        print("--> Аутентификация прошла успешно <--")
                        audit.add_incident(
                            Incident(self.noaccount.login, datetime.datetime.now(), status=self.statusp,
                                     action="login"))
                        audit.add_incident(
                            Incident(self.noaccount.login, datetime.datetime.now(), status=self.statusp,
                                     action="password"))
                        if self.noaccount.int == 0:
                            authorize.access_check(account, self.noaccount.request)
                        else:
                            authorize.access_check(account, interfaceM.user_interaction(account))
                        break

                    else:
                        self.statusp = False
                        break

                else:
                    self.statusl = False

            if not self.statusl:
                audit.add_incident(
                    Incident(self.noaccount.login, datetime.datetime.now(), status=self.statusl, action="login"))
                raise AuthentificationError("!--> Неправильный логин или пароль <--!")
            elif not self.statusp:
                if self.statusl:
                    audit.add_incident(
                        Incident(self.noaccount.login, datetime.datetime.now(), status=self.statusl, action="login"))
                    audit.add_incident(
                        Incident(self.noaccount.login, datetime.datetime.now(), status=self.statusp, action="password"))
                    raise AuthentificationError("!--> Неправильный логин или пароль <--!")
            elif self.statusl:
                pass  # так надо не спрашивай
            else:
                audit.add_incident(
                    Incident(self.noaccount.login, datetime.datetime.now(), status=self.statusp, action="password"))

        except AuthentificationError:
            print("!--> Неправильный логин или пароль <--!")


class Authorization:
    status = 2

    def access_check(self, account, resource_request):
        if len(account.groups) > 0:
            for group in account.groups:
                if resource_request in group.rights:
                    self.status = 0
                    print("Доступ разрешён!")
                    audit.add_incident(Incident(user_name=account.username, time=datetime.datetime.now(),
                                                status='True', action=f"Authorized to {resource_request}"))
                    break
                else:  # в каких-то хоть группах
                    for db_group in db.groups:
                        if resource_request in db_group.rights:
                            self.status = 1
                            break
            if self.status == 1:
                print("Нет прав для выполнения")
                audit.add_incident(Incident(user_name=account.username, time=datetime.datetime.now(),
                                            status=False, action=f"Authorized to {resource_request}"))
            elif self.status == 2:
                print("Нет такого действия")
                audit.add_incident(Incident(user_name=account.username, time=datetime.datetime.now(),
                                            status=False, action=f"Authorized to {resource_request}"))
        else:
            print("Нет прав для выполнения")
            audit.add_incident(Incident(user_name=account.username, time=datetime.datetime.now(),
                                        status=False, action=f"Authorized to {resource_request}"))


class Incident:
    username: Account
    time: datetime
    status: bool
    action: str

    def __init__(self, user_name, time, status, action):
        self.username = user_name
        self.time = time
        self.status = status
        self.action = action


class Audit:
    incidents: list[Incident] = list()

    def get_incidents(self):
        for incident in self.incidents:
            if incident.status:
                print(f'<------------------> {incident.time} | user: \'{incident.username}\' | action: '
                      f'{incident.action} | ip: 127.0.0.1 <----------------->')
            else:
                print(f'<####-ERROR-#######> {incident.time} | user: \'{incident.username}\' | action: '
                      f'{incident.action} | ip: 127.0.0.1 <#################>')

    def add_incident(self, incident):
        self.incidents.append(incident)


########################################################################################################################
audit = Audit()
###
db = Database()
###
authorize = Authorization()
###
noaccountmain = NoAccount()
###
groupadmin = Group(name='groupadmin',
                   rights=['kill', 'word'])
groupuser = Group(name='users',
                  rights=['google', 'ya.oru'])
db.add_group(groupadmin)
db.add_group(groupuser)
###
# db.gen_users()
###
testuser = Account(username='l',
                   password='p',
                   groups=[groupadmin, groupuser])
someuser = Account(username='lol', password='p', groups=[])  # groupuser])
db.add_account(testuser)
db.add_account(someuser)
###
db.output()
###
# interfaceU = CLIUserInput()
interfaceM = CLIUserStub()
###
# a = Authentication(interfaceU.begin_user_interaction(some_noaccount=noaccountmain))
# a.credentials_check(db)
a = Authentication(
    interfaceM.begin_user_interaction(login='lol', password='p', request='ya.oru'))  # <- введите данные для авторизации
a.credentials_check(db)
###
audit.get_incidents()
