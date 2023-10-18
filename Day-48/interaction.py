from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
try:
    driver.get('https://www.linkedin.com/home')
    
    
    
except:
    print('error')

    
driver.quit()


