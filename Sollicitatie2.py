print('Beantwoord, de volgende reeks vragen met: Zelf ingevulde getallen & Ja of Nee. ')

man = input('Is uw gender man? ')
if man == ("Ja"):
    dieren_dressuur = input('Heeft u, ervaring in dieren-dressuur? ')
    if dieren_dressuur == ("Ja"):
        jaar = int(input('Hoeveel, jaar ervaring heeft u? '))
        if jaar >= 4:
            snor = input('Heeft u een snor? ')
            if snor == ("Ja"):
                lengte = int(input('Hoelang is uw snor? '))
                if lengte >= 150:
                    kg = int(input('Hoeveel weegt u? '))
                    if kg >= 90:
                        certificaat = input('Heeft een certificaat voor "Overleven met gevaarlijk personeel" ? ')
                        if certificaat == ("Ja"):
                            print('Gefeliciteerd, u bent aangenomen!! ')
                        else:
                            print('Als u, het certificaat "Overleven met gevaarlijk personeel" nog behaald kunt u op gesprek. ')
                    else:
                        kg < 90
                        print('U moet wat kilootjes aankomen, probeer daarna weer opnieuw. ')
                else:
                    anders = input('U, komt helaas niet in aanmerking met deze vacature wilt aan andere vacature proberen. ')   
                    if anders == ("Nee"):
                        print('Een Fijne dag veder!! ')

            else:
                print('Sorry, u voldoet niet aan de cretirea, een fijne dag veder. ')    
        elif jaar < 4:    
            anders = input ('U, heeft niet genoeg ervaring, wilt een andere vacature proberen? ')
            if anders == ("Nee"):
                print('Dan wensen wij u nog een fijne dag veder.')
            else:
                jongeleren = input('Wilt u, jongeleren proberen? ')
                if jongeleren == ("Ja"):
                    jaar = input('Hoeveel, jaar ervaring heeft u? ')
                else:
                    acrobatiek = input('Wilt, u anders de vacatuere bekijken vooe Acrobatiek? ')
                    if acrobatiek == ("Nee"):
                        print('Onze excuses dat er geen vactature bij zit die u zint, wij wensen u veder een prettige dag veder. ')
                    else:
                        jaar = input('Hoeveel, jaar ervaring heeft u? ')
    
    elif dieren_dressuur == ("Nee"):
        jongeleren = input('U, komt niet in aanmerking voor deze vacature wilt jongeleren proberen? ')
        if jongeleren == ("Ja"):
            jaar = input('Hoeveel, jaar ervaring heeft u met jongeleren? ')
        else:
            acrobatiek = input('Wilt, u anders de vacatuere bekijken vooe Acrobatiek? ')
            if acrobatiek == ("Ja"):
                jaar = input('Hoeveel jaar heeft u ervaring in Acrobatiek? ')
            else:
                print('Onze excuses dat er geen vactature bij zit die u zint, wij wensen u veder een prettige dag veder. ')

elif man == ("Nee"):
    vrouw = input('Is uw gender vrouw? ')
    if vrouw == ("Ja"):
        dieren_dressuur = print('Heeft u, ervaring in dieren-dressuur? ')
    else:
        anders = input('Is uw gender anders dan de voorgaande vragen? ')
        if anders == ("Ja"):
            dieren_dressuur = print('Heeft u, ervaring in dieren-dressuur? ')
        else:
            door = input('Wilt u als nog door gaan? ')
            if door == ("Nee"):
                print('Onze excuses dat u der niet bij zat, wij wensen u nog een fijn dag veder.')
            else:
                dieren_dressuur = print('Heeft u, ervaring in dieren-dressuur? ')
        

geslacht = input("ben je man  vrouw of anders")
