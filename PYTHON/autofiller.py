from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the web driver (make sure you have the driver executable installed)
driver = webdriver.Chrome()

# Open the form URL
driver.get("https://example.com/form")

# Find and fill the input fields
name_input = driver.find_element_by_id("name")
name_input.send_keys("John Doe")

email_input = driver.find_element_by_id("email")
email_input.send_keys("johndoe@example.com")

# Submit the form
submit_button = driver.find_element_by_id("submit")
submit_button.click()

# Wait for a while (adjust as needed)
time.sleep(5)

# Close the web driver
driver.quit()
