import sqlite3
from random import shuffle, randint


def create_connection():
    con = sqlite3.connect('1.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    user_tg_id TEXT,
    user_fio TEXT,
    user_phone
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT
        )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,            
            category_id INTEGER,
            executer TEXT NULL,
            FOREIGN KEY (category_id) REFERENCES categories (id)
            )''')
    return con

def add_user_to_bd(user_data):
    connection = create_connection()
    categories = ('Shar', 'Idsk', 'add_user_to_bd', 'usb', 'Clock', 'INVENTORY')
    tasks = list(categories[:])
    shuffle(tasks)
    user_query = '''INSERT into users values(?,?,?)'''
    categories_query = '''INSERT into categories(category) values(?)'''
    tasks_query = '''INSERT INTO tasks (task, category_id) VALUES (?, ?)'''
    with connection:
        connection.execute(user_query, user_data)
        for category in categories:
            connection.execute(categories_query, (category,))
        for task in tasks:
            connection.execute(tasks_query, (task, randint(1, 6)))


def is_executor():
    connection = create_connection()
    query = '''SELECT * FROM users WHERE user_tg_id=?'''
    id = 193293589,
    with connection:
        a = connection.execute(query, id)
    if a.fetchone() == None:
        return False
    else:
        return True

def get_task(category):
    connection = create_connection()
    categories_query = '''SELECT * FROM categories WHERE category=?'''
    tasks_query = '''SELECT * FROM tasks WHERE category_id=?'''
    with connection:
        category_id = connection.execute(categories_query, (category,))
        id = category_id.fetchone()
        tasks = connection.execute(tasks_query, (id[0],))
    return tasks.fetchall()

'''if __name__=='__main__':
    print(get_task('INVENTORY'))'''
