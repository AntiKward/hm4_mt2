""" БД - База Данных """
""" СУБД - Система Управления Базами Данных"""
""" CRUD - CREATE, RETRIVE, UPDATE, DELETE"""

import sqlite3

connect = sqlite3.connect('geeks.db')
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS geeks(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          full_name VARCHAR (30) NOT NULL,
          age INT DEFAULT NULL,
          direction TEXT,
          is_have BOOLEAN NOT NULL DEFAULT FALSE,
          raiting DOUBLE (4,2) DEFAULT (0.0),
          birth_date DATE
    )
               """)

def register():
  full_name = input("Введите ФИО: ")
  age = int(input("Введите возраст: "))
  direction = input('Ведите направление: ')
  is_have = bool(input("Наличие ноутбука: "))
  rating = float(input("Введите свой рейтинг: "))
  birth_date = input("Введите дату рождения: ")
  
  # cursor.execute(f""" INSERT INTO geeks
  #                (full_name,age,direction,is_have,raiting,birth_date)
  #                VALUES ('{full_name}', {age}, '{direction}', {is_have}, {rating}, '{birth_date}')""")
  # connect.commit()

register()