import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pg

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.monkeytype.com/")
driver.maximize_window()
ac = driver.find_element("xpath", "//button[@class='active acceptAll']")
time.sleep(1)
ac.click()

def t():
    txt=""
    first=a=driver.find_element("xpath", "//div[@class='word active']")
    pg.write(first.text + " ")
    # rest=driver.find_elements("xpath", "//div[@class='word']")
    
    # for b in rest:
    #  pg.write(b.text + " ")er  
    t()
t()
    

        


