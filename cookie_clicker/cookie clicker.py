from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://orteil.dashnet.org/experiments/cookie/')
time.sleep(2)
big_cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

timeout = time.time()+5
while True:
    big_cookie.click()
    if time.time() >= timeout:
        timeout = time.time()+5
        num_of_cookies = int(driver.find_element(By.ID, 'money').text)
        store = driver.find_elements(By.CSS_SELECTOR, '#store b')
        prices = [i.text for i in store]
        for i in range(len(store),-1,-1):
            try:
                if int(prices[i].split()[2]) < num_of_cookies:
                    store[i].click()
                    break
            except:
                pass