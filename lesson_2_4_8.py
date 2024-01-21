# https://stepik.org/lesson/181384/step/8?unit=156009
# 28.99898028271904

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    # говорим WebDriver ждать все элементы в течение 12 секунд
    browser.implicitly_wait(12)
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button = browser.find_element(By.CSS_SELECTOR, "button#book")
    button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button.click()
    # Чтобы из окна alert не копировать цифры для ответа на задание их можно вывести
    alert_obj = browser.switch_to.alert
    msg = alert_obj.text
    print(msg)

finally:
    time.sleep(100)
    browser.quit()