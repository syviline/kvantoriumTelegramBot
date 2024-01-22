import sqlite3

# Функция для подключения к базе данных
def connect_db():
    conn = sqlite3.connect('your_database.db')
    return conn

# Функция для создания таблиц
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Создание таблицы пользователей
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        chat_id INTEGER UNIQUE,
        role TEXT,
        name TEXT,
        age INTEGER,
        parent_name TEXT,
        contact_info TEXT
    )''')

    # Создание других таблиц по мере необходимости

    conn.commit()
    conn.close()

# Функция для добавления нового пользователя
def add_user(chat_id, role, name, age=None, parent_name=None, contact_info=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (chat_id, role, name, age, parent_name, contact_info)
                      VALUES (?, ?, ?, ?, ?, ?)''', (chat_id, role, name, age, parent_name, contact_info))
    conn.commit()
    conn.close()

# Функции для получения данных, обновления информации и других операций с БД

# Вызовите create_tables при первом запуске
create_tables()
