# Import Modules
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL
url = ("https://overwatchleague.com/en-us/schedule?stage=regular_season&")

# Ask which week to be viewed out of a total of 27 weeks
week = int(input('Which week do you want to view, there are 27 weeks? '))

# Obtaining data from url
driver = webdriver.Chrome(' ')# Insert file path
driver.get(url)

# Giving time to find div class
driver.implicitly_wait(15)

# Finding match results
xpath, xpath2 = '//*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[', ']/div/section/div[3]'
fullXpath = xpath + str(week) + xpath2
match = driver.find_element(By.XPATH, fullXpath)

# Formatting output
scores = match.text
results = ' '.join(scores.split('\n'))

print(results)

