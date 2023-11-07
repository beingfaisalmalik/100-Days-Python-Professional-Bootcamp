from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
CAR_DIC = {}

class SingleCarScrapper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=self.options)
        self.image_links = []
    def Scrapper(self,link):
                # Print or process the URL as needed
                self.timeout = 30
                self.driver.get(link)
                time.sleep(30)
                element_present = EC.presence_of_element_located((By.XPATH,'//*[@id="layout-desktop"]/aside/section[1]/div[1]/div[1]/h2'))
                WebDriverWait(self.driver, self.timeout).until(element_present)
                price = self.driver.find_element(By.XPATH,'//*[@id="layout-desktop"]/aside/section[1]/div[1]/div[1]/h2')
                CAR_DIC['price'] = price.text
                name = self.driver.find_element(By.XPATH,'//*[@id="layout-desktop"]/aside/section[1]/section/p')
                CAR_DIC['name'] = name.text
                mileage = self.driver.find_element(By.XPATH,'//*[@id="layout-desktop"]/article/section[2]/ul/li[1]/span/p')
                CAR_DIC['mileage'] = mileage.text
                engine = self.driver.find_element(By.XPATH,'//*[@id="layout-desktop"]/article/section[2]/section/dl[1]/div[3]/dd')
                CAR_DIC['engine'] = engine.text
                model = self.driver.find_element(By.XPATH,'//*[@id="layout-desktop"]/article/section[2]/ul/li[2]/span/p')
                CAR_DIC['model'] = model.text
                
                # gallery_button = driver.find_element(By.XPATH,'//*[@id="layout-desktop"]/article/section[1]/div/div[1]/div[1]/button[2]')
                # gallery_button.click()
                # time.sleep(10)
                gallery_images = self.driver.find_elements(By.TAG_NAME, "img")
                print(len(gallery_images))
                for source_element in gallery_images:
                    srcset_value = source_element.get_attribute("src")
                    self.image_links.append(srcset_value)
                CAR_DIC['images'] = self.image_links
                time.sleep(10)
                return CAR_DIC
                
        