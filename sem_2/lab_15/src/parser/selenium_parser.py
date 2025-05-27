# src/parser/selenium_parser.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_data():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://example.com")
    products = []
    users = []

    product_elements = driver.find_elements(By.CLASS_NAME, 'product')
    for product_element in product_elements:
        name = product_element.find_element(By.CLASS_NAME, 'name').text
        price = float(product_element.find_element(By.CLASS_NAME, 'price').text)
        category = product_element.find_element(By.CLASS_NAME, 'category').text
        products.append((name, price, category))

        user_element = product_element.find_element(By.CLASS_NAME, 'user')
        username = user_element.text
        users.append(username)

    driver.quit()
    return products, users