from getDriver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = get_driver("https://automated.pythonanywhere.com/")


def define_clean_text(text):
    output = text.split(":")
    return float(output[1])

def main():
    time.sleep(2)
    dynamic_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="displaytimer"]'))
    )
    return (define_clean_text(dynamic_text.text))

print(main())