# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the apple homepage
driver.get("https://www.apple.com/ca/")
driver.maximize_window()  # Maximizing the browser window
time.sleep(5)

# Clicking on the "watch" link on the header
todays_offers_link = driver.find_element("xpath","/html/body/div[1]/nav/div/ul/li[2]/div/div/div[5]/ul/li[1]/a/span[1]")
todays_offers_link.click()

# Waiting for the page to load
time.sleep(5)

# Clicking on "watch altra" link
three_for_21_link = driver.find_element("xpath","/html/body/nav/div/ul/li[1]/a/figure")
three_for_21_link.click()

# Waiting for the page to load
time.sleep(10)

# # Selecting a product from the  results
# # Product_link = driver.find_element_by_css_selector("span[data-component-type='s-product-image'] a")
product_link = driver.find_element("xpath","/html/body/main/section[1]/div/div[2]/div/div/div[2]/picture/img")
# # Product_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
product_link.click()
#
#
# #
time.sleep(10)


# Clicking on the why this apple watch
size_button = driver.find_element("xpath", "/html/body/nav/div/div[2]/div[2]/div[1]/ul/li[2]/a")
size_button.click()

# Waiting for the size selection to take effect
time.sleep(10)

# # Adding the Product to buy
add_to_Buy_button = driver.find_element("xpath","/html/body/nav/div/div[2]/div[2]/div[2]/div[2]/a")
add_to_Buy_button.click()
time.sleep(5)

# # Clicking on the titanium case with green alpoine loop
Login_button = driver.find_element("xpath","/html/body/div[2]/div[2]/div[4]/div/div/div/div[2]/div/div/div[2]/ul/li[1]/div/div[1]/img")
actions = ActionChains(driver)
actions.move_to_element(Login_button).click().perform()
time.sleep(5)


# Closing the webdriver
driver.quit()