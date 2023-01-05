#logining with password!
nicks = ['siteers']
data = {'name':'',
'surname':'',
'nick':'',
'password':'',

}
surname = True
name = True
nick = True
while name and surname:
    name = input('Enter your name')
    data['name'] = name
    surname = input('Podaj nazwisko')
    data['surname'] = surname
    break
while nick:
    nick = input('Enter your nick')
    if nick in nicks:
        print(f'Nick {nick} already in use')
    else:
        nicks.append(nick)
        data['nick']=nick
        break

print('set password')
password = input('********')
print('password saved. account created!')
data['password']=password
logining = input('Do you want to sign in (y/sn)?')
if logining == 'y':
    login = input('Login:')
    if login in data['nick']:
        password_2 = True
        while password_2:
            password_2 = input('Password:')
            if password_2 == data['password']:
                print(f'Hello, {data["nick"]}')
                print(f'Do you want to see your data?')
                show_data = input('(yes/no)')
                if show_data == 'yes':
                    print(data)
                break
            else:
                x = 0
                while x < 2:
                    print('Password incorrect, try again')
                    x = x + 1
                    print(f'Its {x} attempts, if 3 account will be block')
                    password_3 = input('try your password again')
                    if password_3 == data['password']:
                        print(f'Hello, {data["nick"]}')
                        print(f'Do you want to see your data?')
                        show_data = input('(yes/no)')
                        if show_data == 'yes':
                            print(data)
                        break
                    elif x == 2:
                        print('account blocked')
            break
                        
                    

elif logining == 'q':
    print('See you later!')

class konta():
    def __init__(self,im,na,log):
        self.im=im
        self.na=na
        self.log=log
    def opis(self):
        print(f'Hello, {self.im.title()} {self.na.title()}!')
konto1=konta(name,surname,nick)
konto1.opis()