import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

class JsonPlaceholderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Placeholder Fetcher")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Введите ID:").pack(pady=5)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        tk.Button(self.root, text="Получить данные", command=self.fetch_data).pack(pady=5)

        self.result_text = tk.StringVar()
        self.result_label = tk.Label(self.root, textvariable=self.result_text, justify="left", wraplength=380)
        self.result_label.pack(pady=10)

    def fetch_data(self):
        user_id = self.entry.get()
        if not user_id.isdigit():
            messagebox.showerror("Ошибка", "Введите корректный ID (число).")
            return

        url = f"https://jsonplaceholder.typicode.com/todos/{user_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.result_text.set(json.dumps(data, indent=4))
            self.save_data(user_id, data)
        else:
            messagebox.showerror("Ошибка", "Не удалось получить данные.")

    def save_data(self, user_id, data):
        folder = "json_data"
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, f"user_{user_id}.json")

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo("Сохранение", f"Данные сохранены в {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = JsonPlaceholderApp(root)
    root.mainloop()
