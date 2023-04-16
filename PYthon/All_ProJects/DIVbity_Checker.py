
#*Let's GO >------->
#!>=======================================================================>
# *Divisiblity Checker!! <===>

#No. Input fron User
noi = input('No. Please- ')
noi = int(noi)

#func That Checks The Divisiblity
def Div_Check(noi):
    print('Your No is- ', noi )
    divd = noi % 2
    if divd == 0:
        print(' Its Div By All Evens ')
    elif divd == 3:
        print(' Its Div By 3 ')
    elif noi % 5 == 0:
        print(' Its Div By 5 ')
    elif noi % 7 == 0:
        print(' Its Div By 7 ')
    elif noi % 9 == 0:
        print(' Its Div By 9 ')
    elif noi % 11 == 0:
        print(' Its Div By 11 ')
    else:
        print('noPE')
    return 'Allright'

#*Using The FunC
print(Div_Check(noi))
#*ProJect_End <===>
#!>=======================================================================>
