# Задание: Управление задачами (To-Do List)
# Описание задачи: Создайте базу данных для управления списком задач. Таблица должна содержать следующую информацию:
# ID задачи (уникальный идентификатор)
# Описание задачи
# Статус задачи (например, «выполняется», «завершена»)
# Дата создания задачи
# Требования:
# Используйте SQLite для создания базы данных.
# Реализуйте следующие функции:
# Добавление новой задачи.
# Обновление статуса задачи.
# Удаление задачи по её ID.
# Просмотр всех задач с сортировкой по дате создания.
# Дополнительное задание (по желанию):
# Реализуйте функцию поиска задач по статусу (например, вывести все завершённые задачи).
# Рекомендации:
# Используйте библиотеку sqlite3 для работы с базой данных.
# Можно создать простое текстовое меню, через которое пользователь может взаимодействовать с программой (добавление, обновление, удаление задач).

import sqlite3
connect=sqlite3.connect('home_work6.db')
cursor=connect.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS to_do_list(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        status BOOLEAN NOT NULL DEFAULT FALSE,
        date DATE)
""")

def register():
    description=input('Описание задачи:')
    status=bool(input('Введите статус задачи:'))
    date=input('Введите дату создание задачи:')

    cursor.execute("""INSERT INTO to_do_list
                   (description, status, date)
                   VALUES (?, ?, ?)""", (description, status, date))
    connect.commit()

def update_task_status(new_status, task_id):
    cursor.execute("""
        UPDATE to_do_list 
        SET status = ? 
        WHERE id = ?
    """, (new_status, task_id))
    connect.commit()
        
def delete_task(task_id):
    cursor.execute("DELETE FROM to_do_list WHERE id=?", (task_id,))
    connect.commit()

def all_tasks():
    cursor.execute("SELECT *FROM to_do_list")
    tasks=cursor.fetchall()
    print(tasks)

def find(status):
    cursor.execute("SELECT * FROM to_do_list WHERE status = ?", (status,))
    tasks = cursor.fetchall()
    for task in tasks:
        return f"ID: {task[0]}, Описание: {task[1]}, Статус: {'Выполняется' if task[2] else 'Завершена'}, Дата: {task[3]}"
   
register()
print(find(True))
update_task_status(True, 1)
delete_task(1)
all_tasks()