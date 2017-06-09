"""
Author: Anestis Karasaridis
The script takes user input and works in two modes:
1)If a state registration number is provided,
it validates it. The program doesn't take into account 
the lenght of specific months, but only a generic form
of 12-month-long year and 31-day-long month. The output in this case is
whether the state reg. nr. is valid or not.
2)If the initial input is left empty, the program requests a birth number
and the user's sex, and outputs a generated sample state reg. nr.

The original assignment required the input to go from the command line,
which I couldn't implement well in the later form of this code with sys.argv.

A better version of this code would also validate the specific birthdate (whether
it is a leap year, and if the days fit in the given month).

Assignment source: https://github.com/engetoacademy/hackathontask

Description in Slovak below:
#číslo musí obsahovať 10 čisel (pre ľudí, ktorí sa narodili po roku 1954)
#alebo musí osahovať 9 čisel (pre ľudí, ktorí sa narodili do roku 1953)
#číslo má 2 časti - dátum narodenia a kontrolný súčet (CCCC) v tvare YYMMDD/CCCC
#celé číslo musí byť delitelné číslom 11
#ženy majú v mesiaci narodenia pridanú hodnotu 50
#
#861107/2239 je validné rodné číslo pre muža, ktorý sa narodil 7.11.1986. 
#025226/1313 je validné rodné číslo ženy narodenej 26.02.2002.
#0 5 2  1 1
# 2 2 6  3 3
#Pre spustenie overenia rodného čísla použijeme príkaz:
# $ birthnumber.py YYMMDD/CCCC
#
# Provided birth number is INVALID.
# <reason>
# <another-reason>
#
#Pre generovanie to bude interaktívny proces:
#
# $ birthnumber.py
#výstup:
#
#Day of the birth [YYYY-MM-DD]: <user input>
#Sex [M/F]: <user input>
#Generated birth number: YYMMDD/CCCC
"""
from random import randrange

def return_c(year):
    if year <= 1953:
        c = randrange(100, 1000)
    else:
        c = randrange(1000, 10000)
    return c

def get_bd2(x):
    # budu se ptat na datum narozeni, dokud nedostanu neco ve formatu YYYY-MM-DD
    # pote jej rozdelim na jednotlive tri casti - dale se to meni podle toho,
    # zda rok<=1953, nebo rok>1953 (to ovlivni, jestli to CCCC bude mit 3 nebo 4 znaky)
    # pak se zeptam na M/F a pripadne m zvysim o 50
    # pak budu randomizovat CCCC(CCC) dokud to cele neni delitelne 11...
    # a nakonec vratim nove rodne cislo
    a = 0
    for i in x:
        if i in '1234567890':
            a += 1
    if len(x)!=10 or x[4]!='-' or x[7]!='-' or a!=8:
        get_bd2(input('1Day of the birth [YYYY-MM-DD]: '))
    else:
        ys, ms, ds = x.split('-')
        yi, mi, di = int(ys), int(ms), int(ds)
        if yi not in range(1000,10000) or mi not in range(1,13) or di not in range(1,32):
            get_bd2(input('2Day of the birth [YYYY-MM-DD]: '))
        else:
            sex = input('Sex [M/F]: ').upper()
            while sex not in "MF":
                sex = input('Sex [M/F]: ').upper()
            if sex == "F":
                mi += 50

            c = return_c(yi)
            first_nr_output = ys+str(mi)+ds+str(c)
            while int(first_nr_output) % 11 != 0:
                c = return_c(yi)
                first_nr_output = ys + str(mi) + ds + str(c)
            print("Generated birth number: "+ys + str(mi) + ds + "/" + str(c))

# vysledkem je fce rozlisujici mezi tvorbou rodneho cisla a validaci rodneho cisla
# nejdriv budu validovat, zda se jedna o jeden ze dvou OK formatu, cimz se spusti funkce na validaci RC nebo fce na tvorbu RC
# funkce tvorba rodneho cisla TRC, funkce validace rodneho cisla VRC
# ta VRC - input ma 11 nebo 10 znaku (6+lomitko+3 nebo 4) - siclice za sebou jsou delitelne 11
def VRC(n):
    b,c=n[:6],n[7:]
    k=int(b+c)%11
    if k==0:
        return 'Provided birth number is VALID.'
    else:
        return 'Provided birth number is INVALID.'

def check_nr_to_proceed(x):
    a=0
    for i in x:
        if i in '1234567890':
            a+=1
    if (len(x)==11 or len(x)==10) and x[6]=='/' and (a==10 or a==9):
        print(VRC(x))
# elif podminka pro tvorbu rc:
        # return fci, ktera tvori rc
    elif x=='':
        get_bd2(input('Day of the birth [YYYY-MM-DD]: '))
    else:
        print('crappy input')
def VRC_test():
    print('Test 01:', VRC('991213/1130') == 'Provided birth number is VALID.')
    print('Test 02:', VRC('991213/1119') == 'Provided birth number is VALID.')
    print('Test 03:', VRC('991213/1118') == 'Provided birth number is INVALID.')
    print('Test 04:', VRC('991213/1117') == 'Provided birth number is INVALID.')
    print('Test 05:', VRC('991213/1116') == 'Provided birth number is INVALID.')
    print('Test 06:', VRC('991213/1115') == 'Provided birth number is INVALID.')
    print('Test 07:', VRC('991213/1114') == 'Provided birth number is INVALID.')
    print('Test 08:', VRC('861107/2239') == 'Provided birth number is VALID.')
    print('Test 09:', VRC('025226/1313') == 'Provided birth number is INVALID.')
    print('Test 10:', VRC('736028/5163') == 'Provided birth number is VALID.')
    print('Test 11:', VRC('521013/119') == 'Provided birth number is VALID.')
    print('Test 12:', VRC('521013/130') == 'Provided birth number is VALID.')
    print('Test 13:', VRC('521013/111') == 'Provided birth number is INVALID.')
    print('Test 14:', VRC('521013/112') == 'Provided birth number is INVALID.')
    print('Test 15:', VRC('521013/113') == 'Provided birth number is INVALID.')
    print('Test 16:', VRC('521013/114') == 'Provided birth number is INVALID.')

# VRC_test()
def check_nr_to_proceed_test():
    print('Test 01:', check_nr_to_proceed('991213/1130') == 'Provided birth number is VALID.')
    print('Test 02:', check_nr_to_proceed('991213/1119') == 'Provided birth number is VALID.')
    print('Test 03:', check_nr_to_proceed('991213/1118') == 'Provided birth number is INVALID.')
    print('Test 04:', check_nr_to_proceed('991213/1117') == 'Provided birth number is INVALID.')
    print('Test 05:', check_nr_to_proceed('991213/1116') == 'Provided birth number is INVALID.')
    print('Test 06:', check_nr_to_proceed('991213/1115') == 'Provided birth number is INVALID.')
    print('Test 07:', check_nr_to_proceed('991213/1114') == 'Provided birth number is INVALID.')
    print('Test 08:', check_nr_to_proceed('861107/2239') == 'Provided birth number is VALID.')
    print('Test 09:', check_nr_to_proceed('025226/1313') == 'Provided birth number is INVALID.')
    print('Test 10:', check_nr_to_proceed('736028/5163') == 'Provided birth number is VALID.')
    print('Test 11:', check_nr_to_proceed('521013/119') == 'Provided birth number is VALID.')
    print('Test 12:', check_nr_to_proceed('521013/130') == 'Provided birth number is VALID.')
    print('Test 13:', check_nr_to_proceed('521013/111') == 'Provided birth number is INVALID.')
    print('Test 14:', check_nr_to_proceed('521013/112') == 'Provided birth number is INVALID.')
    print('Test 15:', check_nr_to_proceed('521013/113') == 'Provided birth number is INVALID.')
    print('Test 16:', check_nr_to_proceed('521013/114') == 'Provided birth number is INVALID.')
    print('Test 17:', check_nr_to_proceed('5210a3/114') == 'crappy input')
    print('Test 18:', check_nr_to_proceed('521013a114') == 'crappy input')
    print('Test 19:', check_nr_to_proceed('521013/a14') == 'crappy input')
    print('Test 20:', check_nr_to_proceed('11') == 'crappy input')
    print('Test 21:', check_nr_to_proceed('111111//11') == 'crappy input')
    print('Test 22:', check_nr_to_proceed('asdaaaaaaa') == 'crappy input')


check_nr_to_proceed(input())