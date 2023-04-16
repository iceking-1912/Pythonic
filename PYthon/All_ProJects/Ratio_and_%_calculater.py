
# Ratio And Percent Calculater

x = input('x -? ')
#to make x int
x = int(x)

y = input('y -? ')
#to make x int
y = int(y)

ratio = (x / y)

percent = (x / y)*100
#formating float
format_float = "{:.5f}".format(percent)

#User Option
useroption = input('0 for Ratio and  1 for Percent -? ')

if useroption == '0':
    print("Ok!")
    print('x/y : Ratio - ')
    print(ratio)
    print('Over')
elif useroption == '1':
    print('Ok!')
    print('% - Percent - ')
    print(percent )
    print('Over')
else:
    print('Invalid Input !!')

#Code Over
# ------------------------------------------------------------------------