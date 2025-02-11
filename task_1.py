import sys
import os
import json
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class JsonPlaceholderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JSON Placeholder Fetcher")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Введите ID:")
        layout.addWidget(self.label)

        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        self.button = QPushButton("Получить данные")
        self.button.clicked.connect(self.fetch_data)
        layout.addWidget(self.button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def fetch_data(self):
        user_id = self.entry.text()

        if not user_id.isdigit():
            QMessageBox.critical(self, "Ошибка", "Введите корректный ID (число).")
            return

        url = f"https://jsonplaceholder.typicode.com/todos/{user_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            formatted_data = json.dumps(data, indent=4)
            self.result_label.setText(formatted_data)
            self.save_data(user_id, data)
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось получить данные.")

    def save_data(self, user_id, data):
        folder = "json_data"
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, f"user_{user_id}.json")

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        QMessageBox.information(self, "Сохранение", f"Данные сохранены в {file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JsonPlaceholderApp()
    window.show()
    sys.exit(app.exec())
