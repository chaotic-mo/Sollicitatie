print('Beantwoord, de volgende reeks vragen met: Zelf ingevulde getallen & Ja of Nee. ')

def dieren():
    dieren_dressuur = input('Heeft u praktijkervaring in dieren dressuur? ')
    if dieren_dressuur == ("Ja"):
        jaar = int(input('Hoeveel jaar ervaring heeft u? '))
        if jaar >= 4:
            if gender == ("Man"):
                snor = input('Heeft u een snor? ')
                if snor == ("Ja"):
                    breed = int(input('Hoe veel cenitimeter is uw Snor? '))
                    if breed >= 10:
                        lang = int(input('Hoe lang bent u? '))
                        if lang >= 150:
                            zwaar = int(input('Hoe hoeveel weegt u? '))
                            if zwaar >= 90:
                                vraag = input('Heeft een, "Overleven met gevaarlijk personeel" certificaat? ')
                                if vraag == ("Ja"):
                                    print('Hoera!, u bent aan genomen!! we kijken er uit naar ons gesprek! ')
                                else:
                                    print('U, hoeft alleen de certificaat te behalen en neem de vragenlijst opnieuw door.')
                        else:
                            print('U moet helaas iets langer zijn.')
                    else:
                        print('U moet helaas een langere snor hebben. ')
                else:
                    print('Helaas, moet u een snor hebben om hier aan mee te doen. ')
            elif gender == ("Vrouw"):
                krull_rood_haar = input('Heeft u lang krull rood haar? ')
                if krull_rood_haar == ("Ja"):
                    lengte = int(input('Hoe veel hoelang is uw haar? '))
                    if lengte >= 10:
                        print('nananan')
                    else:
                        print('U moet uw haar langer laten groeien. ')
                else:
                    print('Helaas, u moet de aangevraagde kleur en type haar hebben. ')
        else:
            wilt = input('Wilt u anders de vacature: jongleren of acrobatiek proberen?')  
            if wilt == ("jongeleren"):
                jongleren()
            elif wilt == ("acrobatiek"):
                acrobatiek()
            else:
                print('Fijna dag veder!! ')
    elif dieren_dressuur == ("Nee"):
        print('Probeer een andere vacature')
    else:
        print('Een fijne dag veder!. ')

def jongleren():
    jongl = input('Heeft u praktijk in Jongleren ? ')
    if jongl == ("Ja"):
        jaar = int(input('Hoeveel jaar ervaring heeft u? '))
        if jaar >= 5:
            snor = input('Heeft u een snor? ')
            if snor == ("Ja"):
                breed = int(input('Hoe veel cenitimeter is uw Snor? '))
                if breed >= 10:
                    lang = int(input('Hoe lang bent u? '))
                    if lang >= 150:
                        zwaar = int(input('Hoe hoeveel weegt u? '))
                        if zwaar >= 90:
                            vraag = input('Heeft een, "Overleven met gevaarlijk personeel" certificaat? ')
                            if vraag == ("Ja"):
                                print('Hoera!, u bent aan genomen!! we kijken er uit naar ons gesprek! ')
                            else:
                                print('U, hoeft alleen de certificaat te behalen en neem de vragenlijst opnieuw door.')
                    else:
                        print('U moet helaas iets langer zijn.')
                else:
                    print('U moet helaas een langere snor hebben. ')
            else:
                print('Helaas, moet u een snor hebben om hier aan mee te doen. ')
        else:
            print('Probeer een andere vacature. ')    
    elif jongl == ("Nee"):
        print('Probeer een andere vacature')
    else:
        print('Een fijne dag veder!. ')

def acrobatiek():
    acro = input('Heeft u praktijk in dieren dressuur? ')
    if acro == ("Ja"):
        jaar = int(input('Hoeveel jaar ervaring heeft u? '))
        if jaar >= 3:
            snor = input('Heeft u een snor? ')
            if snor == ("Ja"):
                breed = int(input('Hoe veel cenitimeter is uw Snor? '))
                if breed >= 10:
                    lang = int(input('Hoe lang bent u? '))
                    if lang >= 150:
                        zwaar = int(input('Hoe hoeveel weegt u? '))
                        if zwaar >= 90:
                            vraag = input('Heeft een, "Overleven met gevaarlijk personeel" certificaat? ')
                            if vraag == ("Ja"):
                                print('Hoera!, u bent aan genomen!! we kijken er uit naar ons gesprek! ')
                            else:
                                print('U, hoeft alleen de certificaat te behalen en neem de vragenlijst opnieuw door.')
                    else:
                        print('U moet helaas iets langer zijn.')
                else:
                    print('U moet helaas een langere snor hebben. ')
            else:
                print('Helaas, moet u een snor hebben om hier aan mee te doen. ')
        else:
            print('Probeer een andere vacature. ')    
    elif acro == ("Nee"):
        print('Probeer een andere vacature')
    else:
        print('Een fijne dag veder!. ')

gender = input('Bent u Man, Vrouw of Anders? ')
dieren()




# if gender == ("Man"):
#     dieren()
# elif gender == ("Vrouw"):
#     female = input('Bent u, female? ')
#     if female == ("Ja"):
#         dieren()
#     else:
#         anders = input('Is uw gender anders dan man of vrouw? ')
#         if anders == ("Ja"):
#             dieren()
#         else:
#             print('Mijn excuses dat u er niet tussen staat, we gaan ons best doen om alles te update!!. ')

