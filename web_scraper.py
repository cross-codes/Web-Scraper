# web_scraper.py
'''
Link for documentation on Selenium and locating via XPath: https://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath
'''

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import prettytable


driver = webdriver.Chrome(os.getcwd() + 'chromedriver')

BASE_URL = "https://www.myntra.com/shoes?p="

for i in range(1, 5):
    print ("Currently on page: ", i)
    driver.get(BASE_URL + str(i))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
    # Because Myntra's page is dynamic, this ensures that all entries load by scrolling down to the bottom

    resultset = driver.find_elements(By.CLASS_NAME, "product-base")
    skip_count = 0
    sneaker_params = {}

    for shoe in resultset:
        try:
            split_data = shoe.text.split('\n')
            rating = split_data[0]
            shoe_name = split_data[3] + " - " + split_data[4]
        except:
            skip_count = skip_count + 1
            continue

        if "sneaker" in shoe_name.lower():    
            sneaker_params[shoe_name] = rating
    
    print ("Skipped ", skip_count, " entries due to missing information.")

print (sneaker_params)

# There is no true "category" of shoes within the pages itself, so we use a default category of "sneakers".

driver.close()







