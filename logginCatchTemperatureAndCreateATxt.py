from time import sleep

from getDriver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dt
import time
driver = get_driver('https://automated.pythonanywhere.com/login/')

def login():
    logginCamp = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="id_username"]'))
    ).send_keys('automated')
    passwordCamp = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="id_password"]'))
    ).send_keys('automatedautomated' + Keys.RETURN)


def catchTemperature():
    sleep(2)
    temperatureValue = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="displaytimer"]'))
    ).text.split(":")[1]
    return(temperatureValue)

def create_txt(temperature):
    filename = f"{dt.now().strftime("%Y-%m-%d.%H-%M-%S")}.txt"
    txt = open(filename,'w+')
    txt.write(temperature)
    txt.close()

def main():
    login()
    temperature = catchTemperature()
    txtCreate = create_txt(temperature)
    print(temperature)
main()