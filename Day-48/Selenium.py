from selenium import webdriver
from selenium.webdriver.common.by import By
import math
driver = webdriver.Chrome()
driver.get("https://www.python.org/")
 
# get element 
dates = driver.find_elements(By.CSS_SELECTOR ,"ul li time")
names = driver.find_elements(By.CSS_SELECTOR ,"ul li time ~ a")
data = {}
for i in range(5,10):
    data[i-5] = {'time':dates[i].text, 'name':names[i].text}
print(data)
driver.quit()