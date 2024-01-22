
import subprocess

#TODO Make App More Accessable

appop = input('1for Zoom,\
2 For Terminal, \
3 For Chrome\
What U Want To Open-')

appop=int(appop)

if appop == 1:
    subprocess.call("C:\\Users\\Himanshu_1912\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    print("ok Opening Zoom!")
elif appop == 2:
    subprocess.call("C:\\cygwin64\\bin\\mintty.exe -i /Cygwin-Terminal.ico -")
    print("ok Opening Terminal!")
elif appop == 3:
    subprocess.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
    print("ok Opening Chrome!")
else:
    print("Soory!")