from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_currency_rate():
    url = "https://www.xe.com/currencyconverter/"  # Замени на актуальный сайт
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)
        time.sleep(5)  # Ожидание загрузки страницы
        rate_element = driver.find_element(By.CLASS_NAME, "result__BigRate-sc-1bsijpp-1")  # Замени на актуальный селектор
        print(f"Курс валют: {rate_element.text}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    get_currency_rate()
