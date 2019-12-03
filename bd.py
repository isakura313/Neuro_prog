import sqlite3

conn = sqlite3.connect("mydatabase.db")  # это у нас коннект с нашей базой данных.
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE IF NOT EXISTS data1 (Id , f, ff) """)


input_data = [
    (1, '13', '13'),
    (1, '15', '15'),
    (1, '16', '16')
]


# print("сколько данных вы хотите ввести?")
# x = int(input())
sql_insert_query = 'INSERT INTO data1 (Id, f, ff)  VALUES (?, ?, ?)'

result = cursor.executemany(sql_insert_query, input_data)

def get_input(x):
    for i in range(x):
        input_var = input()
        input_data.append(input_var)
    print(input_data)

# Сохраняем изменения
# get_input(x)

result = cursor.executemany(sql_insert_query, input_data)
conn.commit()


data = input("введите айди товара")


def get_information(data1):
    sql = "SELECT * FROM shop WHERE id=?"
    cursor.execute(sql, [data])
    print(cursor.fetchall())  # or use fetchone()

get_information(data);

# conn.commit()