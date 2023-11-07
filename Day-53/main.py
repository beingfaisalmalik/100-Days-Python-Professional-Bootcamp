from links import Links
from CarData import SingleCarScrapper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import time
list_of_links = []
list_of_data = []
link = Links()
car = SingleCarScrapper()
list_of_links  = link.links()

with open('Day-53/links.txt', "w") as file:
    # Loop through the list and write each link to a separate line
    for link in list_of_links:
        file.write(link + '\n')

with open('Day-53/links.txt', 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Remove leading and trailing whitespace (e.g., newline characters)
                link = line.strip()
                car_dic = car.Scrapper(link=link)
                list_of_data.append(car_dic)

print(list_of_data)
file = open('Day-53/output.csv', 'a', newline ='')

with file:
    # identifying header  
    header = ['Price', 'name', 'mileage','engine','model','images']
    writer = csv.DictWriter(file, fieldnames = header)
    
    # writing data row-wise into the csv file
    writer.writeheader()
    
    for i in range(len(list_of_data)):
        writer.writerow({'Price' : list_of_data[i]['price'], 
                    'name': list_of_data[i]['name'], 
                    'mileage': list_of_data[i]['mileage'],
                    'engine' : list_of_data[i]['engine'], 
                    'model': list_of_data[i]['model'], 
                    'images': list_of_data[i]['images']})