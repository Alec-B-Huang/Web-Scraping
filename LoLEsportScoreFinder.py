# Import Modules
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL
url = "https://lolesports.com/schedule?leagues=season_2023_kickoff,lcs"

# Obtaining data from url
driver = webdriver.Chrome('C:\\Program Files (x86)\\chromedriver.exe')
driver.get(url)

# Giving time to find div class
driver.implicitly_wait(15)

# Finding match results
match = driver.find_elements(By.CLASS_NAME, "EventMatch")

# Formatting output
#scores = match.text
#results = ' '.join(scores.split('\n'))
blank = []
for result in match:
    blank.append(result.text)

for line in blank:
    new_line = line.replace('\n', ' ')
    print(new_line)
