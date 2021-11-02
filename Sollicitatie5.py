print('Beantwoord, de volgende reeks vragen met: Zelf ingevulde getallen & Ja of Nee. ')

gender = input('Bent u Man, Vrouw of Anders? ')

questions = (
    'Bent u in bezit van een MBO-4 ondernemen diploma? ',
    'Bent u in bezit van een Rijbewijs? ',
    'Bent u in bezit van hoge hoed? ',
    'Bent u in bezit van een certificaat "Overleven met gevaarlijk personeel"? '
)
#Hier maak ik een array aan.
arry = []

for question in questions:
    answer = input(question)

    arry.append(answer)

print(arry)

passed = True

#voor elk anwtoord dat de gebruiekr heeft gegeven 
for answer in arry:
    if answer != ("ja"):
        passed = False
        break


#if passed:

if passed:
    print('Je bent geslaagd!! ')
else:
    print('Je bent gezakt!! =) ')