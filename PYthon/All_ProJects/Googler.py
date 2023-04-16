
#*>>===================================================================================>>

#*Here Is A Googler Who Uses selenium and 
#TODOMake It for More Browser !!
# +Importing Modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

# +Driver
ser = Service("C:\\Users\\hande\\CODE\\Lets_Code\\D-C++_Py_JS_Algo_DS_ETC\\PYthon\\Learning\\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

URL = "https://github.com"

# +Opening Google Web
driver.get(URL)

# ?Sleeping While Wed is Loading
sleep(2)

# +Find Q element
fq = driver.find_element_by_name("q")

# +Geting Query From User
Query = input("What U Want To Search- ")

# +Typing Query
fq.send_keys(Query)

# +Searching It
fq.send_keys(Keys.ENTER)

print("#Scucesfull")

#*>>===================================================================================>>