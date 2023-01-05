#autorski logowanie z hasłem!
nicki=['siteers']
dane={'imie':'',
'nazwisko':'',
'nick':'',
'haslo':'',

}
nazwisko=True
name=True
nick=True
while name and nazwisko:
    name=input('Podaj imię')
    dane['imie']=name
    nazwisko = input('Podaj nazwisko')
    dane['nazwisko']=nazwisko
    break
while nick:
    nick = input('Podaj nick')
    if nick in nicki:
        print(f'Nick {nick} zajęty! Podaj inny nick')
    else:
        nicki.append(nick)
        dane['nick']=nick
        break

print('Nadaj hasło!')
password=input('********')
print('Hasło zapisane, konto utworzone!')
dane['haslo']=password
logining=input('Zalogować się (t/n)?')
if logining == 't':
    login=input('Podaj login!')
    if login in dane['nick']:
        hasloo=True
        while hasloo:
            hasloo=input('Podaj hasło')
            if hasloo == dane['haslo']:
                print(f'Witaj, {dane["nick"]}')
                print(f'Czy chcesz wyświetlić swoje dane?')
                pokazdane=input('(tak/nie)')
                if pokazdane == 'tak':
                    print(dane)
                break
            else:
                x=0
                while x<2:
                    print('haslo niepoprawne spróbuj ponownie')
                    x=x+1
                    print(f'To {x} próba, za 3 będzie blokada konta')
                    haslooo=input('Podaj hasło ponownie')
                    if haslooo == dane['haslo']:
                        print(f'Witaj, {dane["nick"]}')
                        print(f'Czy chcesz wyświetlić swoje dane?')
                        pokazdane=input('(tak/nie)')
                        if pokazdane == 'tak':
                            print(dane)
                        break
                    elif x == 2:
                        print('konto zablokowane')
            break
                        
                    

elif logining=='q':
    print('Do zobaczenia później!')

class konta():
    def __init__(self,im,na,log):
        self.im=im
        self.na=na
        self.log=log
    def opis(self):
        print(f'Witaj, {self.im.title()} {self.na.title()}!')
konto1=konta(name,nazwisko,nick)
konto1.opis()