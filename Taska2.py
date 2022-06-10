from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

try: 
    link = "https://www.yandex.ru"
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    browser.get(link)

    browser.find_element(By.XPATH,'//input[@class="input__control input__input mini-suggest__input"]').send_keys("Planet for me")
    browser.find_element(By.XPATH,'//div[@class="search2__button"]').click()
    browser.find_element(By.LINK_TEXT, 'planetfor.me').click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    browser.find_element(By.XPATH,'//input[@class="ml-8"]').send_keys('qa'+ Keys.ENTER)
    
finally:
    time.sleep(10)
    browser.quit()
    