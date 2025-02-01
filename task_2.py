from docx import Document
import tkinter as tk
from tkinter import simpledialog

def create_word_file(user_input):
    doc = Document()
    doc.add_paragraph(user_input)
    file_name = "output.docx"
    doc.save(file_name)
    return file_name

def on_button_click():
    user_input = simpledialog.askstring("Input", "Введите текст для сохранения в Word-файл:")
    if user_input:
        file_name = create_word_file(user_input)
        result_label.config(text=f"Word-файл '{file_name}' успешно создан.")

root = tk.Tk()
root.title("Word File Creator")

button = tk.Button(root, text="Создать Word-файл", command=on_button_click)
button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
