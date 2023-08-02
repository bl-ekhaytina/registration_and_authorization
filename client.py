from tkinter import *
from server import insert_variable_into_table, find_variable_in_table, connection, hash


def click_on_buttonRegistration():
    login = entryLogin.get(1.0, END).rstrip('\n')
    password = entryPassword.get(1.0, END).rstrip('\n')
    insert_variable_into_table(login, password)


def click_on_buttonAuthorization():
    login = entryLogin.get(1.0, END).rstrip('\n')
    password = entryPassword.get(1.0, END).rstrip('\n')
    num = find_variable_in_table(login)
    h = hash(hash(password) + hash(str(num)))
    if connection(login, h):
        labelConnection['text'] = "Соединение установлено"
    else:
        labelConnection['text'] = "Неверный пароль"


"""GUI"""
root = Tk()
root.geometry("500x500")

label2 = Label()
label2['text'] = "Логин:"
label2.place(x=100, y=100)

entryLogin = Text(width=20, height=1)
entryLogin.insert(1.0, "admin")
entryLogin.place(x=170, y=100)

label22 = Label()
label22['text'] = "Пароль:"
label22.place(x=100, y=160)

entryPassword = Text(width=20, height=1)
entryPassword.insert(1.0, "admin")
entryPassword.place(x=170, y=160)

buttonRegistration = Button(text="Регистрация")
buttonRegistration.config(command=click_on_buttonRegistration)
buttonRegistration.place(x=100, y=220)

buttonAuthorization = Button(text="Авторизация")
buttonAuthorization.config(command=click_on_buttonAuthorization)
buttonAuthorization.place(x=250, y=220)

labelConnection = Label()
labelConnection.place(x=100, y=270)

root.mainloop()
