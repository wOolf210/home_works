from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_marketplace_prices():
    url = "https://www.example.com/category"  # Замени на актуальный маркетплейс
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)
        time.sleep(5)  # Ожидание загрузки страницы
        prices = driver.find_elements(By.CLASS_NAME, "product-price")  # Замени на актуальный селектор

        for price in prices:
            print(f"Цена: {price.text}")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    get_marketplace_prices()
