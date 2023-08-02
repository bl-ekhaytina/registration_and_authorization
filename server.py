import sqlite3
import hashlib
import random
from tkinter import messagebox


"""ХЕШИРОВАНИЕ"""
def hash(string):
    hash_object = hashlib.md5(string.encode())
    return hash_object.hexdigest()


"""СОЗДАНИЕ ТАБЛИЦЫ"""
def create_table():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("CREATE TABLE table2 (login TEXT PRIMARY KEY, password TEXT, label TINYINT);")
        sqlite_connection.commit()
        print("Таблица создана")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


"""РЕГИСТРАЦИЯ"""
def insert_variable_into_table(login, password):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        sqlite_insert_with_param = """INSERT INTO table2
                                      (login, password)
                                      VALUES (?, ?);"""
        data_tuple = (login, hash(password))
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Данные занесены в таблицу")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


"""ЗАНЕСЕНИЕ МЕТКИ В ТАБЛИЦУ"""
def find_variable_in_table(login):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT login FROM table2 WHERE login == ?;", [login])
        res = cursor.fetchone()
        try:
            if res[0] == login:
                num = random.randint(0, 255)
                print(num)
            cursor.execute("UPDATE table2 SET label == ? WHERE login == ?;", [hash(str(num)), login])
            sqlite_connection.commit()
            print("Метка занесена в таблицу")
        except:
            messagebox.showwarning("Ошибка", "Логин не найден")
        finally:
            cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
        return num


"""АВТОРИЗАЦИЯ"""
def connection(login, h):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT password FROM table2 WHERE login == ?;", [login])
        password_local = cursor.fetchone()
        cursor.execute("SELECT label FROM table2 WHERE login == ?;", [login])
        label_local = cursor.fetchone()
        h_local = hash(password_local[0] + label_local[0])
        if h == h_local:
            return 1
        else:
            return 0
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
