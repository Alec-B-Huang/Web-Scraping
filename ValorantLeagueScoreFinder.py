# Import Modules
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL
url = "https://valorantesports.com/standings"

# Obtaining data from url
driver = webdriver.Chrome('C:\\Program Files (x86)\\chromedriver.exe')
driver.get(url)

# Giving time to find div class
driver.implicitly_wait(15)

# Finding match results
match = driver.find_element(By.CLASS_NAME, "e631e")

# Formatting output
scores = match.text
results = ' '.join(scores.split('\n'))

# Display output
print(results)