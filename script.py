from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
service = Service("./chromedriver.exe")

def get_driver(name):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service,options=options)
    driver.get("https://www.merxenergia.com.br/")
    return driver
def main():
   driver = get_driver()
   element = WebDriverWait(driver,10).until(
       EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/section[1]/section/div[1]/p'))
   )
   return element.text


print(main())