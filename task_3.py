import requests
from bs4 import BeautifulSoup

url = "https://example.com/weather/astana"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Найдем элементы с нужной информацией
    location = soup.find("div", class_="location").text.strip()
    condition = soup.find("span", class_="condition").text.strip()
    temperature = soup.find("span", class_="temperature").text.strip()

    print("Местоположение:", location)
    print("Состояние погоды:", condition)
    print("Температура:", temperature)
else:
    print("Ошибка при запросе данных:", response.status_code)
