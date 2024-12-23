from selenium import webdriver
from selenium.webdriver.chrome.service import  Service

service = Service("./chromedriver.exe")

def get_driver(name):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service,options=options)
    driver.get(name)
    return driver