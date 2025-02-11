import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range(start="2024-01-01", periods=100)
products = ["Телефон", "Ноутбук", "Планшет", "Наушники", "Часы"]
sales_data = pd.DataFrame({
    "Дата": np.random.choice(dates, 100),
    "Товар": np.random.choice(products, 100),
    "Цена": np.random.randint(5000, 100000, 100),
    "Количество": np.random.randint(1, 10, 100)
})

sales_data["Сумма"] = sales_data["Цена"] * sales_data["Количество"]

avg_price = sales_data["Цена"].mean()
median_price = sales_data["Цена"].median()
max_price = sales_data["Цена"].max()
min_price = sales_data["Цена"].min()
total_revenue = sales_data["Сумма"].sum()

print(f"📊 Средняя цена: {avg_price:.2f}")
print(f"📊 Медианная цена: {median_price}")
print(f"📊 Макс. цена: {max_price}, Мин. цена: {min_price}")
print(f"📊 Общая выручка: {total_revenue}")

plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
sales_data["Товар"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Количество продаж по товарам")

plt.subplot(1, 3, 2)
sales_data.groupby("Дата")["Сумма"].sum().plot(kind="line", marker="o", color="green")
plt.title("Выручка по дням")

plt.subplot(1, 3, 3)
sales_data.groupby("Товар")["Сумма"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Доля продаж по товарам")

plt.tight_layout()
plt.show()
