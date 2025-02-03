import os
import json
import time
import requests
import asyncio
import aiohttp


URL = "https://jsonplaceholder.typicode.com/posts"
FOLDER_NAME = "json_data"


def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def fetch_json_sync():
    start_time = time.time()

    response = requests.get(URL)
    if response.status_code == 200:
        os.makedirs(FOLDER_NAME, exist_ok=True)
        data = response.json()

        for item in data:
            save_json(item, os.path.join(FOLDER_NAME, f"post_{item['id']}.json"))

    print(f"Синхронная загрузка завершена за {time.time() - start_time:.2f} сек.")


async def fetch_post_async(session, post_id):
    async with session.get(f"{URL}/{post_id}") as response:
        if response.status == 200:
            data = await response.json()
            save_json(data, os.path.join(FOLDER_NAME, f"post_{post_id}.json"))


async def fetch_json_async():
    start_time = time.time()
    os.makedirs(FOLDER_NAME, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_post_async(session, post_id) for post_id in range(1, 101)]
        await asyncio.gather(*tasks)

    print(f"Асинхронная загрузка завершена за {time.time() - start_time:.2f} сек.")


if __name__ == "__main__":
    print("Запуск синхронной загрузки...")
    fetch_json_sync()

    print("\nЗапуск асинхронной загрузки...")
    asyncio.run(fetch_json_async())

    print("\nПрограмма завершена.")