import requests

# Делаем запрос к статическому сайту погоды (предполагаем, что сайт существует)
url = "https://example.com/weather/astana"  # Замените на реальный URL
response = requests.get(url)

if response.status_code == 200:
    weather_data = response.text  # Получаем HTML-ответ

    # Пример использования string.split()
    parts = weather_data.split()  # Разделяем строку на элементы
    location = parts[0]           # Пример: это может быть имя города
    condition = parts[1]          # Пример: это описание состояния погоды
    temperature = parts[2]        # Пример: это температура

    print("Местоположение:", location)
    print("Состояние погоды:", condition)
    print("Температура:", temperature)
else:
    print("Ошибка при запросе данных:", response.status_code)
