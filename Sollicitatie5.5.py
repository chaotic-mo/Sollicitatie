#direct aangeven wat ergaat gebeuren.
print('Vacature: circusdirecteur voor circus hoteldebotel.''\n' 
      'Hier komen de vragen voor een paar vacatures graag zo eerlijk mogelijk beantworden.')
#een vraag voor welke gender dat de gebruiker moet in vullen.
gender = input('Bent u Man, Vrouw of Anders? ')

#Hier maak ik een lege array aan.
array = []

gewicht = int(input('Wat is uw gewicht in hele kilograms? '))
if gewicht >= 90:
    array.append("ja")
else:
    array.append("nee")

lengte =  int(input('Wat is uw lichaams lengte in hele centimeters? '))
if lengte >= 150:
    array.append("ja")
else:
    array.append("nee")
#Hier komen de vragen voor de genders.
if gender == ("Man"):
    snor = input('Heeft u een snor? ')
    if snor == ("ja"):
        breedte = int(input('Hoeveel cenitmeter breed is uw snor? '))
        if breedte >= 10:
            array.append("ja") 
        else:
            array.append("nee")
    else:
        array.append("nee")
        print('Groei een snor!! ') 
elif gender == ("Vrouw"):
    R_Krul_haar = input('Heeft u rood krul haar? ')
    if R_Krul_haar == ("ja"):
        lengte_haar = int(input('Hoeveel centimeter lang is uw haar? '))
        if lengte_haar >= 20:
            array.append("ja")
        else:
            array.append("nee")
    else:
        array.append("nee")
        print('Groei, krull & verf uw haar!! ')
else:
    gender == ("Anders")
    lange_neus = input('Heeft u een lange neus? ')
    if lange_neus == ("ja"):
        lengte = int(input('Hoeveel centimeters is uw neus? '))
        if lengte >= 25:
            array.append("ja")
        else:
            array.append("nee")
    else:
        array.append("nee")
        print('Koop misschien een fop neus? =) ')

#Hier komen de vragen van jaren ervaring.
Dieren_dressuur = int(input('Hoeveel jaar ervaring heeft u in Dieren-dressuur? '))
if Dieren_dressuur >= 4:
    array.append("ja")
else:
    array.append("nee")

Jongeleren = int(input('Hoeveel jaar ervaring heeft u in jongleren? '))
if Jongeleren >= 5:
    array.append("ja")
else:
    array.append("nee")

Acrobatiek = int(input('Hoeveel jaar ervaring heeft u in acrobatiek? '))
if Acrobatiek >= 3:
    array.append("ja")
else:
    array.append("nee")

#Een veriable met daarin de directe vragen
bezit = (
    'Bent u in bezit van een MBO-4 Diploma Ondernemen? ', 
    'Bent u in bezit van een Geldig vrachtwagen rijbewijs? ', 
    'Bent u in bezit van een Hoge hoed? ', 
    'Bent u in bezit van een certificaat "Overleven met gevaarlijkpersoneel"? ')

#Hier vraag de informatie van bezit aan, om de andtwoorden in de array te zetten
for moet in bezit:
    antwoord = input(moet)
    array.append(antwoord.lower())
print(array)

passed = True

for antwoord in array:
    if antwoord != ("ja"):
        passed = False
        break

if passed:
    print('Je, bent geslaagd!! ')
else:
    print('Je, bent gezakt!! =) ')
