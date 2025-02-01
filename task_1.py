import time
import threading
import asyncio
import aiohttp
import requests

URLS = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 101)]


def fetch_url(url):
    response = requests.get(url)
    return response.status_code


def download_sequential():
    start_time = time.time()
    for url in URLS:
        fetch_url(url)
    end_time = time.time()
    print(f"Последовательная загрузка завершена. Время выполнения: {end_time - start_time} секунд.")


def download_with_threads():
    start_time = time.time()
    threads = []

    for url in URLS:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Многопоточная загрузка завершена. Время выполнения: {end_time - start_time} секунд.")


async def fetch_url_async(session, url):
    async with session.get(url) as response:
        return response.status


async def download_with_async():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, url) for url in URLS]
        await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Асинхронная загрузка завершена. Время выполнения: {end_time - start_time} секунд.")


if __name__ == "__main__":
    print("Запуск последовательной загрузки...")
    download_sequential()

    print("\nЗапуск многопоточной загрузки...")
    download_with_threads()

    print("\nЗапуск асинхронной загрузки...")
    asyncio.run(download_with_async())
