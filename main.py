import ntplib
from time import ctime
import os
import pickle
terminy = []
nazwyzad = []
lokalizacja = []
terminr = 0
terminm = 0
termind = 0
u = 0
cel = 0
ed = 0
try:
    nazwyzad = pickle.load(open('nazwyzad.dat', 'rb'))
except:
    pickle.dump(nazwyzad, open('nazwyzad.dat', 'wb'))
try:
    terminy = pickle.load(open('terminy.dat', 'rb'))
except:
    pickle.dump(terminy, open('terminy.dat', 'wb'))
try:
    lokalizacja = pickle.load(open('lokalizacja.dat', 'rb'))
except:
    pickle.dump(lokalizacja, open('lokalizacja.dat', 'wb'))
try:
    ListaNR = pickle.load(open('ListaNR.dat', 'rb'))
except:
    ListaNR = []
    pickle.dump(ListaNR, open('ListaNR.dat', 'wb'))

cls = lambda: os.system('cls')

def zegar():
    cls()
    c = ntplib.NTPClient()
    response = c.request('europe.pool.ntp.org', version=3)
    ntplib.ref_id_to_text(response.ref_id)
    print('Obecnie mamy:', ctime(response.tx_time))
    input('Naciśnij Enter aby powrócić do menu')
    mainmenu('nie')

def listaklientow():
    def wypisywanie():
        cls()
        ListaNR = pickle.load(open('ListaNR.dat', 'rb'))
        i = 0
        u = 0
        for i in range(0, int(len(ListaNR) / 2)):
            print(i+1, ListaNR[u],' ',ListaNR[u+1])
            u += 2
        input('Naciśnij Enter aby kontynuować')
        menulista('nie')
    def dodawanie():
        ListaNR = pickle.load(open('ListaNR.dat', 'rb'))
        IN = str(input('Podaj Imie i nazwisko: '))
        NR = str(input('Podaj Numer telefonu: '))
        ListaNR.append(IN)
        ListaNR.append(NR)
        pickle.dump(ListaNR, open('ListaNR.dat', 'wb'))
        menulista('nie')
    def edytowanie():
        cls()
        ListaNR = pickle.load(open('ListaNR.dat', 'rb'))
        i = 0
        u = 0
        nr = 0
        for i in range(0, int(len(ListaNR) / 2)):
            print(i + 1, ListaNR[u], ' ', ListaNR[u + 1])
            u += 2
        while nr < 1 or nr > len(ListaNR)/2:
            nr = int(input('Który wpis chciałbyś edytować? Podaj nr: '))
        x = 0
        while x != 1 and x != 2:
            x = int(input('Co chciałbyś edytować? 1. Imię i Nazwisko 2. nr. telefonu: '))
            if x == 1:
                xx = nr * 2 - 2
            elif x == 2:
                xx = nr * 2 - 1
        y = str(input('Podaj nowe dane: '))
        ListaNR[xx] = y
        pickle.dump(ListaNR, open('ListaNR.dat', 'wb'))
        i = 0
        u = 0
        for i in range(0, int(len(ListaNR) / 2)):
            print(i + 1, ListaNR[u], ' ', ListaNR[u + 1])
            u += 2
        menulista('nie')
    def usuwanie():
        ListaClear = str(input('Czy na pewno chcesz usunąć wpis?: '))
        if ListaClear == 'Tak' or ListaClear == 'tak' or ListaClear == 'T' or ListaClear == 't':
            i = 0
            u = 0
            for i in range(0, int(len(ListaNR) / 2)):
                print(i + 1, ListaNR[u], ' ', ListaNR[u + 1])
                u += 2
            listanr = int(input('Wybierz wpis który chcesz usunąć: '))
            NR = listanr * 2
            b = 0
            while 2 > b:
                b = b+1
                del ListaNR[(NR - 2)]
            pickle.dump(ListaNR, open('ListaNR.dat', 'wb'))
            print('Lista została wyczyszczona')
            menulista('nie')
        else:
            print('Nic nie zostało usunięte')
            menulista('nie')
    def menulista(lblad):
        cls()
        print('1. Wyświetlanie Listy | 2. Dodawanie listy | 3. Edytowanie listy | 4. Czyszczenie listy | 5. Powrót do menu głównego')
        if lblad == 'tak':
            print('Niepoprawna akcja')
        ListaNR = []
        ListaNR = pickle.load(open('ListaNR.dat', 'rb'))
        x = input()
        if x=='1':
            wypisywanie()
        elif x=='2':
            dodawanie()
        elif x=='3':
            edytowanie()
        elif x=='4':
            usuwanie()
        elif x=='5':
            cls()
            mainmenu('nie')
        else:
            menulista('tak')
    menulista('nie')

def listazadan():
    def nowezadanie():
        print('Dodawanie zadania')
        print('Podaj nazwę zadania:')
        nazwazad = input()
        nazwyzad.append(nazwazad)
        print('Podaj lokalizację spotkania:')
        lokalizacjaspo = input()
        lokalizacja.append(lokalizacjaspo)
        print('Podaj termin wykonania:')
        print('Rok:')
        global terminr
        global terminm
        global termind

        def checker():
            global terminr
            terminr = int(input())
            if terminr < 2021:
                print('Podaj poprawny rok')
                checker()

        checker()
        print('Miesiąc (liczba):')

        def checker():
            global terminm
            terminm = int(input())
            if terminm < 1 or terminm > 12:
                print('Podaj poprawny miesiąc')
                checker()

        checker()
        print('Dzień:')

        def checker():
            global termind
            global terminm
            global terminr
            termind = int(input())
            '''boże mój...'''
            if terminm == 1 or terminm == 3 or terminm == 5 or terminm == 7 or terminm == 8 or terminm == 10 or terminm == 12:
                if termind < 1 or termind > 31:
                    print('Podaj poprawny dzień')
                    checker()
            elif terminm == 2:
                if termind < 1 or termind > 29 or termind > 28 and terminr % 4 != 0:
                    print('Podaj poprawny dzień')
                    checker()
            else:
                if termind < 1 or termind > 30:
                    print('Podaj poprawny dzień')
                    checker()

        checker()
        terminr = str(terminr)
        terminm = str(terminm)
        termind = str(termind)
        termin = termind + '.' + terminm + '.' + terminr
        terminy.append(termin)
        pickle.dump(nazwyzad, open('nazwyzad.dat', 'wb'))
        pickle.dump(terminy, open('terminy.dat', 'wb'))
        pickle.dump(terminy, open('terminy.dat', 'wb'))
        pickle.dump(lokalizacja, open('lokalizacja.dat', 'wb'))
        menu('nie')

    def edycjazadania():
        print('Edycja zadania:')
        global terminy
        global ed
        global cel
        global nazwyzad
        i = 0
        for i in range(0, len(nazwyzad)):
            print(i + 1, nazwyzad[i], 'Termin:', terminy[i])
        print('Podaj cel (numer zadania):')

        def checker():
            global cel
            cel = int(input())
            if cel < 1 or cel > len(nazwyzad) + 1:
                print('Podaj poprawny cel')
                checker()
            else:
                print('1. Edycja nazwy zadania 2. Edycja terminu zadania')
                checker2()

        def edzad():
            global cel
            global nazwyzad
            print('Podaj nową nazwę zadania:')
            tempnazw = input()
            nazwyzad[cel - 1] = tempnazw

        def edterm():
            print('Podaj nowy termin:')
            print('Rok:')
            global terminy
            global terminr
            global terminm
            global termind

            def checker():
                global terminr
                terminr = int(input())
                if terminr < 2021:
                    print('Podaj poprawny rok')
                    checker()

            checker()
            print('Miesiąc (liczba):')

            def checker():
                global terminm
                terminm = int(input())
                if terminm < 1 or terminm > 12:
                    print('Podaj poprawny miesiąc')
                    checker()

            checker()
            print('Dzień:')

            def checker():
                global termind
                global terminm
                global terminr
                termind = int(input())
                '''boże mój... Ponownie!'''
                if terminm == 1 or terminm == 3 or terminm == 5 or terminm == 7 or terminm == 8 or terminm == 10 or terminm == 12:
                    if termind < 1 or termind > 31:
                        print('Podaj poprawny dzień')
                        checker()
                elif terminm == 2:
                    if termind < 1 or termind > 29 or termind > 28 and terminr % 4 != 0:
                        print('Podaj poprawny dzień')
                        checker()
                else:
                    if termind < 1 or termind > 30:
                        print('Podaj poprawny dzień')
                        checker()

            checker()
            terminr = str(terminr)
            terminm = str(terminm)
            termind = str(termind)
            termin = termind + '.' + terminm + '.' + terminr
            terminy[cel - 1] = termin

        def checker2():
            global ed
            ed = input()
            if ed == '1':
                edzad()
            elif ed == '2':
                edterm()
            else:
                print('Podaj poprawną akcję')
                checker2()

        checker()
        pickle.dump(nazwyzad, open('nazwyzad.dat', 'wb'))
        pickle.dump(terminy, open('terminy.dat', 'wb'))
        menu('nie')

    def usunieciezadania():
        print('Usuwanie zadania:')
        i = 0
        for i in range(0, len(nazwyzad)):
            print(i + 1, nazwyzad[i], 'Termin:', terminy[i])
        print('Wybierz cel:')
        global u
        u = 0

        def check():
            global u
            u = int(input())
            if u < 1 or u > len(nazwyzad):
                print('Podaj poprawny cel:')
                check()

        check()
        del nazwyzad[u - 1]
        del terminy[u - 1]
        pickle.dump(nazwyzad, open('nazwyzad.dat', 'wb'))
        pickle.dump(terminy, open('terminy.dat', 'wb'))
        menu('nie')

    def wypiszzadania():
        print('Twoje zadania:')
        i = 0
        for i in range(0, len(nazwyzad)):
            print(i + 1, '| Termin:', terminy[i], '| Nazwa:', nazwyzad[i], '| Lokalizacja:', lokalizacja[i])
        dupmvariable = input()
        menu('nie')

    def menu(blad):
        cls()
        if blad == 'tak':
            print('Niepoprawna akcja')
        print('Wybierz akcję: 1.Dodaj zadanie 2.Edytuj istniejące zadanie 3.Usuń zadanie 4.Wypisz zadania 5.Wróć do menu głównego')
        x = input()
        if x == '1':
            nowezadanie()
        elif x == '2':
            edycjazadania()
        elif x == '3':
            usunieciezadania()
        elif x == '4':
            wypiszzadania()
        elif x == '5':
            cls()
            mainmenu('nie')
        else:
            blad = 'tak'
            menu(blad)

    menu('nie')

def mainmenu(mblad):
    cls()
    print('Wybierz akcję: 1. Zegar 2. Lista Klientów 3. Lista spotkań 4. Wyjdź')
    if mblad == 'tak':
        print('Niepoprawna akcja')
    x = input()
    if x=='1':
        zegar()
    elif x=='2':
        listaklientow()
    elif x == '3':
        listazadan()
    elif x=='4':
        cls()
        return 0
    else:
        mainmenu('tak')
mainmenu('nie')
