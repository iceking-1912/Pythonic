                                                                                
# !>>====================================================================>
# *LogIn_ProJects_Dynamic
vuser = ['HimanshuH_1912', 'BharatH_2210', 'Meow', ]
vpassword = [191205, 221001, 270575, ]

# *Input From User
iuser = input('UserName Please- ')
iuser=str(iuser)
ipass = input('PassWord Please- ')
ipass=int(ipass)
#*Initial Values
userok = 0
logon = 0

#*Main_Validater
def m_vd():
    # +Validating User
    for vduser in vuser:
        if vduser == iuser:
            userok = 1
            print()
        # +Validating PassWord
            for vdpass in vpassword:
                if vdpass == ipass:
                    logon = 1
                # +Greeting The User
                    if logon == 1:
                        #  Then Greetings Hence Done Best Through Nesting
                        print("Welcome,", iuser)
                        print('To Our InFiVerse')

#*Initialzing Func
m_vd()

# *Program Ended
#!>>====================================================================>>