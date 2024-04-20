from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
#This line will open the site on chrome
driver.get("https://3dsky.org/")
#The 10 seconds delay allows the page to load, it can be changed depending on your network
time.sleep(10)
products_list = driver.find_elements(By.TAG_NAME, "app-main-new-model")
#The loop does the main task, which is to screenshot the images, get the titles and saves them in an "images" folder.
for product in products_list:
    product_title = product.find_element(By.CSS_SELECTOR, "div > div > a")
    title = product_title.get_property("innerText")
    
    product_image = product.find_element(By.CSS_SELECTOR, "div > a > img")
    
    if product_image.get_attribute("width") == "136" or product_image.get_attribute("widht") == "196":
        product_image.screenshot(f"./images/product_image_{title}.png")
    else:
        pass
#This closes the chrome page.    
driver.quit()
