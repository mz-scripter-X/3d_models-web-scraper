from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, pandas

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://3dsky.org/")
time.sleep(10)
products_list = driver.find_elements(By.TAG_NAME, "app-main-new-model")
#This is the part that gets the image src and title
product_dict = {
    "Product Title": [product.find_element(By.CSS_SELECTOR, "div > div > a").get_property("innerText") for product in products_list],
    "Image Link": [product.find_element(By.CSS_SELECTOR, "div > a > img").get_attribute("src") for product in products_list]
}
#This saves the data into a csv
product_data = pandas.DataFrame(product_dict)
product_data.to_csv("3d_models_pro.csv")

driver.quit()
