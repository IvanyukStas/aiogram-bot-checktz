import sqlite3

def create_connection():
    con = sqlite3.connect('1.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    user_tg_id TEXT,
    user_fio TEXT,
    user_phone
    )''')
    return con

def add_user_to_bd(user_data):
    connection = create_connection()
    user_query = '''INSERT into users values(?,?,?)'''
    with connection:
        connection.execute(user_query, user_data)


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



'''if __name__=='__main__':
    print(is_executor())'''