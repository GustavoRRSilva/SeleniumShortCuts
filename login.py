
from getDriver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = get_driver('https://automated.pythonanywhere.com/login/')

time.sleep(2)
def main():
    logginCamp = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="id_username"]'))
    ).send_keys('automated')

    passwordCamp = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id_password"]'))
    ).send_keys('automatedautomated'+Keys.RETURN)

    signInCamp = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/form/button'))
    ).click()
    input("...")
main()