import tkinter as tk
from tkinter import messagebox
import requests
import json
import os


def fetch_data():
    user_id = entry.get()
    if not user_id.isdigit():
        messagebox.showerror("Ошибка", "Введите корректный ID (число).")
        return

    url = f"https://jsonplaceholder.typicode.com/todos/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result_text.set(json.dumps(data, indent=4))
        save_data(user_id, data)
    else:
        messagebox.showerror("Ошибка", "Не удалось получить данные.")


def save_data(user_id, data):
    folder = "json_data"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, f"user_{user_id}.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    messagebox.showinfo("Сохранение", f"Данные сохранены в {file_path}")


root = tk.Tk()
root.title("JSON Placeholder Fetcher")
root.geometry("400x300")

tk.Label(root, text="Введите ID:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Получить данные", command=fetch_data).pack(pady=5)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", wraplength=380)
result_label.pack(pady=10)

root.mainloop()
