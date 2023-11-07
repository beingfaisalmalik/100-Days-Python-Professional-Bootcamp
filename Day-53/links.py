from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import re
class Links:
    def __init__(self):
        pass
    
    def links(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(options=options)
        

        driver.get('https://www.autotrader.co.uk/')
        timeout = 20
        try:
            element_present = EC.presence_of_element_located((By.NAME, 'postcode'))
            WebDriverWait(driver, timeout).until(element_present)
            select_make = driver.find_element(By.ID, 'make')
            make = Select(select_make)
            make.select_by_value("Volkswagen")
            time.sleep(5)
            select_model = driver.find_element(By.ID, 'model')
            model = Select(select_model)
            model.select_by_value("Caddy Maxi Life")
            time.sleep(5)
            post_code = driver.find_element(By.ID , 'postcode')
            post_code.send_keys('SW1W 0NY')
            time.sleep(5)
            search_button = driver.find_element(By.XPATH,'/html/body/div/main/div/header/div[2]/div/div/form/div[2]/div[2]/button')
            search_button.click()
            time.sleep(30)
            pages = driver.find_element(By.CSS_SELECTOR,'p[data-testid="pagination-show"]')
            match = re.search(r"Page (\d+) of (\d+)", pages.text)

            if match:
                page_number = match.group(1)
                total_pages = match.group(2)
            links = []

        

            for i in range(1,int(total_pages)+1):
                anchor_elements = driver.find_elements(By.CSS_SELECTOR,'a[data-testid="search-listing-title"]')
                for anchor_element in anchor_elements:
                    href_attribute = anchor_element.get_attribute("href")
                    links.append(href_attribute)
                links.pop()
                links.pop()
                if i !=12:
                    next_page = driver.find_element(By.CSS_SELECTOR,'a[data-testid="pagination-next"]')
                    next_page.click()
                    time.sleep(20)
                else:
                    print('Done ')
            driver.quit()
            return links
        except TimeoutException:
            print("Timed out waiting for page to load")

