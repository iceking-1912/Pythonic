
# *it is copied from python-import which is cloned from git/CoreyMScharfer/cosw-Snipets

print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1

# *SCT Finder


def SCTVF(*ang):
    if type(*ang) == int:
        import math
        sinv = math.sin(*ang)
        cosv = math.cos(*ang)
        tanv = math.tan(*ang)
        print('Here Is Your Value of Sin-Cos-Tan of Input(Int) !!')
        print('Sin Value- ', sinv)
        print('Cos Value- ', cosv)
        print('Tan Value- ', tanv)
    else:
        print('error')
    return -1


SCTVF(518)

# a= [631486,68483,661636]

# type(a)

# print(type(a))

# if type(a) == str:
#     print('ok Its A String')
# elif type(a)== int:
#     print('ok Its A Int')
# else :
#     print('nope')
