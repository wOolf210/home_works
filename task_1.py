import os
import shutil
import requests
import asyncio
import aiohttp


def clear_folder(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)


def download_images_sync():
    url = "https://picsum.photos/200/300"
    folder = "images_sync"
    clear_folder(folder)

    for i in range(10):
        response = requests.get(url)
        with open(os.path.join(folder, f"image_{i + 1}.jpg"), "wb") as file:
            file.write(response.content)
    print("Синхронная загрузка изображений завершена.")


async def download_image_async(session, url, folder, i):
    async with session.get(url) as response:
        content = await response.read()
        with open(os.path.join(folder, f"image_{i + 1}.jpg"), "wb") as file:
            file.write(content)


async def download_images_async():
    url = "https://picsum.photos/200/300"
    folder = "images_async"
    clear_folder(folder)

    async with aiohttp.ClientSession() as session:
        tasks = [download_image_async(session, url, folder, i) for i in range(10)]
        await asyncio.gather(*tasks)
    print("Асинхронная загрузка изображений завершена.")


if __name__ == "__main__":
    download_images_sync()
    asyncio.run(download_images_async())
