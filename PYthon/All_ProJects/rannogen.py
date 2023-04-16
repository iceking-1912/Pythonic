
#*>>--------------------------------------------------------------------------------------------->>
#*OTP ProJect
import math , random

rno = ""
ui = input()
valed = 0

def genrno():
    digits = "0123456789"
    global rno
    for grno in range(6):
        rno += digits[math.floor(random.randint(0,9))]
    print("Random No. is " + rno)
    return rno

genrno()

def uival():
    if rno == ui:
        valed = 1
    else:
        print("Nope")
        valed = 0
        
uival()

print(valed)



#*>>--------------------------------------------------------------------------------------------->>