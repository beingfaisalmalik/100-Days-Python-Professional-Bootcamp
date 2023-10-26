from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

user_name = input('Enter Your Username : ')
user_password = input('Enter Your Password : ')
other_user = input('Enter The User To Search : ')
driver.get('https://www.instagram.com/?hl=en')
time.sleep(10)

name = driver.find_element(By.NAME,'username')
name.send_keys(f'{user_name}')
password = driver.find_element(By.NAME,'password')
password.send_keys(f'{user_password}')
button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
button.click()
time.sleep(10)
search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/span/div/a')
search.click()

time.sleep(5)
search = driver.find_element(By.TAG_NAME, 'input')
search.send_keys(f'{other_user}')
time.sleep(5)

print('success')