print('Beantwoord, de volgende reeks vragen met: Zelf ingevulde getallen & Ja of Nee. ')
gender = input('Bent u Man, Vrouw of Anders? ')

welke = input('Welke vacature wilt u: dierendressuur, jongeleren of acrobatiek? ')

def gender_check():
    if gender == ("Man"):
        snor_check()
    elif gender == ("Vrouw"):
        rood_krullhaar_check()
    elif gender == ("Anders"):
        pass

def snor_check():
    snor = input('Heeft u een snor? ')
    if snor == ("Ja"):
        breedte = input('Hoeveel centimeter breed is uw snor? ')
        if breedte >= 10:
            lengte()
        else:
            print('Laat meer breedte over groeien!! ')
    else:
        print('Krijg baard groei ofzoe !! =) ')

def rood_krullhaar_check():
    pass

def snor_check():
    pass

def dieren():
    jaar = int(input('Hoeveel jaar ervaring heeft u? '))
    if jaar >= 4:
        gender_check()

def jongeleren():
    pass

def acrobatiek():
    pass

def lengte():
    pass

def gewicht():
    pass

def certificaat():
    pass

if welke == ("dierendressuur"):
    dieren()
elif welke == ("jongeleren"):
    jongeleren()
elif welke == ("acrobatiek"):
    acrobatiek()
else:
    print('Sorry zoek ergens anders maar een baan!! =) ')

