from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time

username = 'username'
password = 'password'


option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)

driver.get('https://www.instagram.com/')

user_entry = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
user_entry.send_keys(username)

password_entry = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password_entry.send_keys(password)

driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(10)

driver.get('https://www.instagram.com/chefsteps/followers/')  # the page link
time.sleep(10)
followers = driver.find_elements(By.CSS_SELECTOR, '._aano div div button')
print(followers)

for i in followers:
    try:
        i.click()
        time.sleep(1)
    except ElementClickInterceptedException:
        driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]').click()