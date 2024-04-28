
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect(r'Web_site\web\static\database\db.db')
cursor = connection.cursor()

# Создаем таблицу Users
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Report (
# id INTEGER PRIMARY KEY,
# usernum INTEGER,
# pet TEXT NOT NULL,
# place TEXT NOT NULL
# )
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY,
# login TEXT NOT NULL,
# password TEXT NOT NULL,
# agent TEXT NOT NULL,
# email TEXT NOT NULL,
# phone TEXT NOT NULL,
# like TEXT NOT NULL,
# skill TEXT NOT NULL
# )
# ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pets (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
what TEXT NOT NULL,
story TEXT NOT NULL,
sum INTEGER,
forum TEXT NOT NULL
)
''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Donats (
# id_user INTEGER,
# id_pet INTEGER,
# sum INTEGER,
# wish TEXT NOT NULL
# )
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Applications (
# id_user INTEGER,
# id_pet INTEGER,
# years INTEGER,
# fio TEXT NOT NULL,
# statys TEXT NOT NULL,
# home TEXT NOT NULL,
# work TEXT NOT NULL,
# hobby TEXT,
# Allergic TEXT
# )
# ''')
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Applications (
# id_user INTEGER,
# id_pet INTEGER,
# years INTEGER,
# fio TEXT NOT NULL,
# statys TEXT NOT NULL,
# home TEXT NOT NULL,
# work TEXT NOT NULL,
# hobby TEXT,
# Allergic TEXT
# )
# ''')
# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()