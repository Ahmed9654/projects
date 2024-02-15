import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdicr33iQ46H5RKVzNFN47hX0m9JQru4J5qzneKNHZDnRRcgg/viewform')


response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
soup = BeautifulSoup(response.text, 'html.parser')
all_houses = soup.select(selector='.List-c11n-8-84-3-photo-cards li')

# for i in range(len(house))
for i in range(len(all_houses)):
    try:
        house = all_houses[i].select(selector='.StyledPropertyCardDataWrapper')
        link = house[0].a.get('href')
        payment = house[0].select(selector='.PropertyCardWrapper span')[0].get_text()
        address = house[0].find(name='address').get_text()

        answer_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        answer_address.send_keys(address)

        answer_payment = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        answer_payment.send_keys(payment)

        answer_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        answer_link.send_keys(link)

        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
        time.sleep(2)
        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdicr33iQ46H5RKVzNFN47hX0m9JQru4J5qzneKNHZDnRRcgg/viewform')
        time.sleep(2)
    except:
        pass
