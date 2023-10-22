from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(1000)
driver.get('https://fast.com/')

time.sleep(5)
speed = driver.find_element(By.ID, 'speed-value')
t = f' My Internet Speed Is {speed.text} Mbps'

driver.get('https://google.com')
speed_input = driver.find_element(By.NAME,'q')
speed_input.send_keys(t)
speed_input.send_keys(Keys.ENTER)
print('Success')