from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()



try:
    driver.get("https://demoqa.com/text-box")
    print("Title: "+driver.title)
    Header = driver.find_element(By.CLASS_NAME, "text-center")
    driver.implicitly_wait(5)
    print("Header: "+ Header.text)


    FullName = driver.find_element(By.ID,"userName")
    FullName.send_keys("Pavan Kalyan")

    UserEmail = driver.find_element(By.ID, "userEmail")
    UserEmail.send_keys("Pavan@dispostable.com")

    CurrentAddress = driver.find_element(By.ID, "currentAddress")
    CurrentAddress.send_keys("Address - 2:4")

    PermanentAddress = driver.find_element(By.ID, "permanentAddress")
    PermanentAddress.send_keys("Address - 3, 464- street")

    driver.find_element(By.ID,"submit").click()

    Outputs = driver.find_elements(By.XPATH, "//div[@id='output']/div/p")
    for output in Outputs:
        print(output.text)

finally:
    driver.quit()