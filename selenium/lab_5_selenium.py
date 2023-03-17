# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(3)
#
# # Finding the search bar and entering text
# # search_bar = driver.find_element_by_id("id","twotabsearchtextbox")
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("laptop")
#
# # Submitting the search query
search_bar.send_keys(Keys.RETURN)
#
# # Waiting for the search results page to load
time.sleep(5)
#
# # Verifying that the search results page has loaded
assert "laptop" in driver.title
#
# # Selecting a laptop from the search results
# # laptop_link = driver.find_element_by_css_selector("span[data-component-type='s-product-image'] a")
laptop_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div/a[2]/div/div[1]/img")
# # laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
laptop_link.click()
#
#
# # Waiting for the laptop details page to load
time.sleep(5)
#
# # Verifying that the correct laptop details page has loaded
# # assert "laptop" in driver.title
#
# # Adding the laptop to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()
#
# # Waiting for the cart to update
time.sleep(5)
#
# # Clicking on no thanks button
no_thanks_button= driver.find_element("xpath","/html/body/div[5]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span[2]/span/input")
no_thanks_button.click()
time.sleep(2)
#
# # Verifying that the laptop has been added to the cart
cart_count = driver.find_element("id","nav-cart-count")
assert cart_count.text == "1"
#
# # Closing the webdriver
driver.close()
