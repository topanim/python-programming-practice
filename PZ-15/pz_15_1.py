import sqlite3

# Название файла базы данных
DB_NAME = 'tasks.db'

# --- Вспомогательная функция для вывода списка поручений ---
def _display_tasks_list(rows):
    """Форматированно выводит список поручений."""
    if not rows:
        print("Записи не найдены.")
        return
    print("-" * 80)
    print(f"{'ID':<5} | {'Название':<30} | {'Выдано':<10} | {'Срок':<10} | {'Исполнитель':<20}")
    print("-" * 80)
    for row in rows:
        print(f"{row[0]:<5} | {row[1]:<30} | {row[2]:<10} | {row[3]:<10} | {row[4]:<20}")
    print("-" * 80)

# --- Функции для работы с БД ---

def create_table(cursor):
    """Создает таблицу tasks."""
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                issue_date TEXT NOT NULL,
                due_date TEXT NOT NULL,
                assignee TEXT NOT NULL
            )
        ''')
        print("Таблица 'tasks' готова.")
    except sqlite3.Error as e: print(f"Ошибка создания таблицы: {e}")

def add_initial_data(conn, cursor):
    """Добавляет 10 начальных записей, если таблица пуста."""
    try:
        res = cursor.execute("SELECT COUNT(id) FROM tasks").fetchall()
        if res[0][0] == 0:
            tasks = [('Подготовить отчет', '2023-10-26', '2023-11-10', 'Иванов И.И.'), ('Разработать модуль', '2023-10-27', '2023-11-30', 'Петров П.П.'), ('Обновить документацию', '2023-10-27', '2023-11-15', 'Сидоров А.В.'), ('Анализ конкурентов', '2023-10-28', '2023-11-20', 'Иванов И.И.'), ('Настроить CI/CD', '2023-10-28', '2023-12-05', 'Петров П.П.'), ('Написать тесты', '2023-10-29', '2023-11-25', 'Сидоров А.В.'), ('Встреча с заказчиком', '2023-10-30', '2023-11-05', 'Иванов И.И.'), ('Исправить ошибки', '2023-10-30', '2023-11-03', 'Петров П.П.'), ('Подготовить презентацию', '2023-10-31', '2023-11-18', 'Сидоров А.В.'), ('Запланировать спринт', '2023-10-31', '2023-11-02', 'Иванов И.И.')]
            cursor.executemany('INSERT INTO tasks (title, issue_date, due_date, assignee) VALUES (?, ?, ?, ?)', tasks)
            conn.commit()
            print("Добавлены 10 начальных записей.")
        else: print(f"В таблице уже есть записи ({res[0][0]}).") # Повторный select, т.к. fetchone() сдвигает курсор
    except sqlite3.Error as e: print(f"Ошибка добавления начальных данных: {e}"); conn.rollback()

def add_task(conn, cursor):
    """Добавляет новую задачу."""
    print("\n--- Добавление поручения ---")
    title = input("Название: ")
    issue_date = input("Дата выдачи (ГГГГ-ММ-ДД): ")
    due_date = input("Срок (ГГГГ-ММ-ДД): ")
    assignee = input("Исполнитель: ")
    if not all([title, issue_date, due_date, assignee]): print("Ошибка: Все поля обязательны."); return
    try: cursor.execute('INSERT INTO tasks (title, issue_date, due_date, assignee) VALUES (?, ?, ?, ?)', (title, issue_date, due_date, assignee)); conn.commit(); print("Поручение добавлено.")
    except sqlite3.Error as e: print(f"Ошибка добавления: {e}"); conn.rollback()

def display_all_tasks(cursor):
    """Отображает все поручения."""
    print("\n--- Все поручения ---")
    try: cursor.execute("SELECT id, title, issue_date, due_date, assignee FROM tasks"); _display_tasks_list(cursor.fetchall())
    except sqlite3.Error as e: print(f"Ошибка отображения: {e}")

def search_tasks(cursor):
    """Ищет поручения (3 варианта WHERE)."""
    print("\n--- Поиск ---")
    print("1. По ID\n2. По исполнителю (часть)\n3. Срок до даты")
    choice = input("Выбор критерия: ")
    query, params = None, None
    try:
        if choice == '1': task_id = int(input("Введите ID: ")); query, params = "SELECT * FROM tasks WHERE id = ?", (task_id,)
        elif choice == '2': assignee_part = input("Введите часть имени исполнителя: "); query, params = "SELECT * FROM tasks WHERE assignee LIKE ?", (f'%{assignee_part}%',)
        elif choice == '3': due_date_limit = input("Срок до (ГГГГ-ММ-ДД): "); query, params = "SELECT * FROM tasks WHERE due_date <= ?", (due_date_limit,)
        else: print("Неверный выбор."); return
        if query: cursor.execute(query, params); print("\n--- Результаты поиска ---"); _display_tasks_list(cursor.fetchall())
    except ValueError: print("Ошибка: Неверное число.")
    except sqlite3.Error as e: print(f"Ошибка поиска: {e}")

def delete_tasks(conn, cursor):
    """Удаляет поручения (3 варианта WHERE)."""
    print("\n--- Удаление ---")
    print("1. По ID\n2. По исполнителю (часть)\n3. Выданы до даты")
    choice = input("Выбор критерия: ")
    query, params = None, None
    if input("Подтвердите удаление (да/нет): ").lower() != 'да': print("Удаление отменено."); return
    try:
        if choice == '1': task_id = int(input("Введите ID: ")); query, params = "DELETE FROM tasks WHERE id = ?", (task_id,)
        elif choice == '2': assignee_part = input("Введите часть имени исполнителя: "); query, params = "DELETE FROM tasks WHERE assignee LIKE ?", (f'%{assignee_part}%',)
        elif choice == '3': issue_date_limit = input("Выданы до (ГГГГ-ММ-ДД): "); query, params = "DELETE FROM tasks WHERE issue_date < ?", (issue_date_limit,)
        else: print("Неверный выбор."); return
        if query: cursor.execute(query, params); conn.commit(); print(f"Удалено записей: {cursor.rowcount}")
    except ValueError: print("Ошибка: Неверное число.")
    except sqlite3.Error as e: print(f"Ошибка удаления: {e}"); conn.rollback()

def edit_tasks(conn, cursor):
    """Редактирует поручения (3 варианта WHERE)."""
    print("\n--- Редактирование ---")
    print("1. По ID\n2. Изменить исполнителя (выданы до даты)\n3. Изменить срок (по исполнителю)")
    choice = input("Выбор критерия: ")
    query, params = None, None
    try:
        if choice == '1':
            task_id = int(input("Введите ID: ")); cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)); task = cursor.fetchone()
            if not task: print(f"ID {task_id} не найден."); return
            print(f"Текущие: ID: {task[0]}, Название: {task[1]}, Выдано: {task[2]}, Срок: {task[3]}, Исполнитель: {task[4]}")
            field_choice = input("Редактировать поле (1-Название, 2-Выдано, 3-Срок, 4-Исполнитель): ")
            new_value = input("Новое значение: ")
            fields = { '1': 'title', '2': 'issue_date', '3': 'due_date', '4': 'assignee' }
            if field_choice in fields: query, params = f"UPDATE tasks SET {fields[field_choice]} = ? WHERE id = ?", (new_value, task_id)
            else: print("Неверный выбор поля."); return
        elif choice == '2':
            issue_date_limit = input("Выданы до (ГГГГ-ММ-ДД): "); new_assignee = input("Новый исполнитель: ")
            query, params = "UPDATE tasks SET assignee = ? WHERE issue_date <= ?", (new_assignee, issue_date_limit)
        elif choice == '3':
            assignee = input("Исполнитель: "); new_due_date = input("Новый срок (ГГГГ-ММ-ДД): ")
            query, params = "UPDATE tasks SET due_date = ? WHERE assignee = ?", (new_due_date, assignee)
        else: print("Неверный выбор."); return
        if query: cursor.execute(query, params); conn.commit(); print(f"Обновлено записей: {cursor.rowcount}")
    except ValueError: print("Ошибка: Неверное число.")
    except sqlite3.Error as e: print(f"Ошибка редактирования: {e}"); conn.rollback()

# --- Главное меню и цикл ---

def main_menu():
    """Отображает меню."""
    print("\n--- Меню ---")
    print("1. Добавить\n2. Показать все\n3. Найти\n4. Удалить\n5. Редактировать\n0. Выход")
    return input("Выберите действие: ")

def main():
    """Основная функция."""
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME); cursor = conn.cursor()
        create_table(cursor)
        add_initial_data(conn, cursor)
        while True:
            choice = main_menu()
            if choice == '1': add_task(conn, cursor)
            elif choice == '2': display_all_tasks(cursor)
            elif choice == '3': search_tasks(cursor)
            elif choice == '4': delete_tasks(conn, cursor)
            elif choice == '5': edit_tasks(conn, cursor)
            elif choice == '0': print("Выход."); break
            else: print("Неверный ввод.")
    except sqlite3.Error as e: print(f"Ошибка БД: {e}")
    # except Exception as e: print(f"Непредвиденная ошибка: {e}")
    finally:
        if conn: conn.close(); print("Соединение с БД закрыто.")

if __name__ == "__main__":
    main()