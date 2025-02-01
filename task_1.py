import time
import threading
import asyncio
import os


def create_file_with_delay(file_name):
    time.sleep(1)
    with open(file_name, 'w') as f:
        f.write("This is a file created with delay.")


async def create_file_with_delay_async(file_name):
    await asyncio.sleep(1)
    with open(file_name, 'w') as f:
        f.write("This is a file created with delay.")


def delete_files(file_names):
    for file_name in file_names:
        try:
            os.remove(file_name)
        except PermissionError:
            print(f"Ошибка при удалении файла {file_name}: файл занят другим процессом.")


def run_with_delay():
    file_names = []
    start_time = time.time()
    for i in range(100):
        file_name = f"file_{i}.txt"
        create_file_with_delay(file_name)
        file_names.append(file_name)

    end_time = time.time()
    print(f"Все файлы созданы. Время выполнения без многозадачности: {end_time - start_time} секунд.")
    delete_files(file_names)


def run_with_threads():
    file_names = []
    start_time = time.time()

    threads = []
    for i in range(100):
        file_name = f"file_{i}.txt"
        thread = threading.Thread(target=create_file_with_delay, args=(file_name,))
        threads.append(thread)
        thread.start()
        file_names.append(file_name)

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Все файлы созданы. Время выполнения с многопоточностью: {end_time - start_time} секунд.")
    delete_files(file_names)


async def run_with_async():
    file_names = []
    start_time = time.time()

    tasks = []
    for i in range(100):
        file_name = f"file_{i}.txt"
        task = create_file_with_delay_async(file_name)
        tasks.append(task)
        file_names.append(file_name)

    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Все файлы созданы. Время выполнения с асинхронностью: {end_time - start_time} секунд.")
    delete_files(file_names)


if __name__ == "__main__":
    print("Запуск без многозадачности...")
    run_with_delay()
    print("\nЗапуск с многопоточностью...")
    run_with_threads()
    print("\nЗапуск с асинхронностью...")
    asyncio.run(run_with_async())
    print("\nПрограмма завершена.")