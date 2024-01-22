
from selenium import webdriver


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

print("Hi 😁😀")

URL = "https://google.com"


ser = Service("C:\\Users\\hande\\CODE\\Lets_Code\\D-C++_Py_JS_Algo_DS_ETC\\PYthon\\Learning\\chromedriver.exe")

driver = webdriver.Chrome(service=ser)

driver.get(URL)


