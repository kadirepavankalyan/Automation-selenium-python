import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instantiate the WebDriver (make sure chromedriver is in your PATH or provide the path to chromedriver)
driver = webdriver.Chrome()

# Open the practice form URL
driver.get("https://demoqa.com/automation-practice-form")

# Maximize the browser window
driver.maximize_window()

# Scroll down the page
driver.execute_script("window.scrollBy(0, 400);")

# Explicit wait until the first name field is present
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "firstName")))

# Fill out the form
driver.find_element(By.ID, "firstName").send_keys("Pavan")
driver.find_element(By.ID, "lastName").send_keys("Kalyan")
driver.find_element(By.ID, "userEmail").send_keys("Pavan@dispostable.com")

# Explicit wait until the gender radio button is clickable
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@value='Male']")))

# Select the gender radio button
gender_male = driver.find_element(By.XPATH, "//*[@value='Male']")
gender_male.click()

# Fill out the mobile number
driver.find_element(By.ID, "userNumber").send_keys("1234567890")

# Use ActionChains to send the Enter key
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()

# Allow time to observe the result
time.sleep(5)

# Close the browser
driver.quit()
