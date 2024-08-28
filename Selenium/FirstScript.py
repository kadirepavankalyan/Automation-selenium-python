from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Initialize the WebDriver (assuming you have ChromeDriver installed and in your PATH)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

try:
    # Navigate to a webpage (example: Google)
    driver.get("https://www.google.com")

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

finally:
    # Close the browser
    driver.quit()
