# Import Modules
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL
url = ("https://overwatchleague.com/en-us/schedule?stage=regular_season&")

# Obtaining data from url
driver = webdriver.Chrome('C:\\Program Files (x86)\\chromedriver.exe')
driver.get(url)

# Giving time to find div class
driver.implicitly_wait(15)

# Finding match results
match = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[1]/div/section/div[3]/div[3]/div/div[2]')
match = driver.find_element(By.CLASS_NAME, "match-cardstyles__Middle-sc-1rgscfz-6 GRdHe")
#matchs_during_week = driver.find_element((By.XPATH, '//*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[1]/div/section/div[3]').size())

# Formatting output
#games = matchs_during_week.text
scores = match.text
results = ' '.join(scores.split('\n'))

print(results)


#//*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[1]/div/section/div[3]/div[2]/div/div[2]