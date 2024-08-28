import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def log_details():
    logging.basicConfig(
        filename="demo.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H-%M-%S %p'
    )
    return logging.getLogger()


logger = log_details()
logger.info("Program execution started!")

driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to a webpage (example: Google)
driver.get("https://www.google.com")
logger.info("URL passed into the browser")

# Locate the search bar using its name attribute value
search_bar = driver.find_element(By.NAME, "q")

# Enter a search query
search_bar.send_keys("Selenium Python")

# Simulate pressing the Enter key
search_bar.send_keys(Keys.RETURN)

# Wait for the results to load and display the search results
driver.implicitly_wait(5)  # seconds

# Extract search results (e.g., the titles of the results)
results = driver.find_elements(By.XPATH, "//h3")

# Print the title of each search result
for result in results:
    print(result.text)

driver.close()
logger.info("Program ends here")
