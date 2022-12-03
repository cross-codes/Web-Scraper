# web_scraper.py

'''
Link for documentation on Selenium and locating via XPath: https://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath
'''

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from prettytable import PrettyTable


driver = webdriver.Chrome(os.getcwd() + 'chromedriver')

BASE_URL = "https://www.myntra.com/shoes?p="

for x in range(1, 5):
    print ("Currently on page: ", x)
    driver.get(BASE_URL + str(x))
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
    
    print ("Skipped", skip_count, "entries due to missing information.")

# There is no true "category" of shoes within the pages itself, so we use a default category of "sneakers".
file = open("sneakers.csv", "w", newline="")  # Note: "sneakers.csv" will be made in the current directory
writer_object = csv.writer(file)

column_1 = ["Sneaker_Name"] + list(sneaker_params.keys())
column_2 = ["Category", "Sneakers"]
column_3 = ["User_Rating (/5)"] + list(sneaker_params.values())

temp_row = []
summary_table = PrettyTable(["Sneaker_Name", "Category", "User_Rating (/5)"])

for y in range(0, len(column_1), 1):

    temp_row.append(column_1[y])
    if y == 0:
        temp_row.append(column_2[0])
    else:
        temp_row.append(column_2[1])
    temp_row.append(column_3[y])

    writer_object.writerow(temp_row)
    if y > 0:
        summary_table.add_row(temp_row)
    temp_row = []
    

print ("\nThe file has been succesfully created in", os.getcwd(), "\b. A summary of the contents of the file is as shown below:\n", summary_table)

file.flush()
file.close()
driver.close()







