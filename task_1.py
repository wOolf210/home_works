import psycopg2


DB_CONFIG = {
    "dbname": "your_database",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
}


def connect_db():
    return psycopg2.connect(**DB_CONFIG)


def create_table():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    age INTEGER NOT NULL
                )
            """)
            conn.commit()


def create_user(name, age):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id", (name, age))
            user_id = cur.fetchone()[0]
            conn.commit()
            print(f"✅ Пользователь {name} добавлен с ID {user_id}")


def read_all_users():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            for user in users:
                print(user)


def read_one_user(user_id):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            user = cur.fetchone()
            print(user if user else "❌ Пользователь не найден")


def update_user(user_id, new_name, new_age):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, age = %s WHERE id = %s RETURNING id",
                        (new_name, new_age, user_id))
            if cur.fetchone():
                conn.commit()
                print(f"✅ Пользователь {user_id} обновлён")
            else:
                print("❌ Пользователь не найден")


def delete_user(user_id):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s RETURNING id", (user_id,))
            if cur.fetchone():
                conn.commit()
                print(f"✅ Пользователь {user_id} удалён")
            else:
                print("❌ Пользователь не найден")


if __name__ == "__main__":
    create_table()

    # Тестовые операции
    create_user("Иван", 25)
    create_user("Анна", 30)

    print("\n📌 Все пользователи:")
    read_all_users()

    print("\n📌 Один пользователь (ID = 1):")
    read_one_user(1)

    print("\n📌 Обновляем пользователя ID = 1:")
    update_user(1, "Иван Иванов", 26)
    read_one_user(1)

    print("\n📌 Удаляем пользователя ID = 2:")
    delete_user(2)
    read_all_users()
