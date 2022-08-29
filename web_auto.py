from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

PATH = Service("C:/Users/swang/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://amazon.ca")

# Input "bag" in search bar then press ENTER
search = driver.find_element("name", "field-keywords")
search.clear()
search.send_keys("bag")
search.send_keys(Keys.RETURN)
time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "a-fixed-left-grid-col"))
)
# List all titles
titles = driver.find_elements(By.CLASS_NAME, "a-size-base-plus")
for title in titles:
    print(title.text)

# Click one title
link = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div[2]/div[1]/h2/a/span')
link.click()

# Back to last page
driver.back()
driver.forward()

time.sleep(3)
driver.quit()



