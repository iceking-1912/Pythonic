
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#from time import sleep

#TODO Make It More Dynamic!!

ser = Service("C:\\Users\\hande\\CODE\\Lets_Code\\D-C++_Py_JS_Algo_DS_ETC\\PYthon\\Learning\\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

ml = "https://us05web.zoom.us/j/5531371826?pwd=Y0orR2cwMjM3cUoyVGExQUIzTXdUZz09"

cl1 = "https://us02web.zoom.us/j/2509009676?pwd=c2tOMUxXNGdLdS9OSXQzOVhsdmdiZz09"

gg = "https://youtube.com"


sleep(5)

driver.get(gg)

# popuphandler=driver.SwitchTo().popup()
# popuphandler.accept()

#/html/body/div[3]/div[2]/div/div[1]/div

#driver.get(l1)

# def meetop(lop):
#     driver.get(lop)
#     print("Joining The Meeting!!")
#     popuphandler=driver.SwitchTo().Alert()
#     popuphandler.accept()
# ulop = input("'ml'Which Meeting U Want To Join- ")

# if ulop == 1:
#     meetop(ml)
# elif ulop == 2:
#     meetop(cl1)

#driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/h3[2]/span/a").click()
