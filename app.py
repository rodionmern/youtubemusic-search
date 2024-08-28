import YouTubeMusicAPI
import pyperclip
import time
import os

def clearTerm():
    if os.name == "posix":
        os.system("clear")
    if os.name == "nt":
        os.system("cls")

print('''
Добро пожаловать!

0 - Информация о композиции
1 - Выдать обложку композиции
''')

inputOut = input("")

clearTerm()

if inputOut == "0":
    query = input("Введи автора и название композиции: ")
    result = YouTubeMusicAPI.search(query)
    clearTerm()
    if result:
        print(f'Исполнитель: {result.get("name")}')
        print(f'Название композиции: {result.get("title")}')
        print(f'URL адрес: {result.get("url")}')
        print("")
        print("Скопировать ссылку в буфер обмена?")
        copy = input("Y/n: ")
        if copy == "Y" or copy == "y" or copy == "Yes" or copy == "yes":
            clearTerm()
            pyperclip.copy(result.get("url"))
            print("Скопировано.")
            print("")
            print("Программа будет закрыта через несколько секунд..")
            time.sleep(3)
            quit()
        else:
            clearTerm()
            print("Программа будет закрыта через несколько секунд..")
            time.sleep(3)
            quit()
    else:
        print("Композиция не найдена, проверьте входные данные.")
elif inputOut == "1":
    query = input("Введи автора и название композиции: ")
    result = YouTubeMusicAPI.search(query)
    clearTerm()
    if result:
        print(f'Исполнитель: {result.get("name")}')
        print(f'Название композиции: {result.get("title")}')
        print(f'URL обложки: {result.get("artwork")}')
        print("")
        print("Скопировать ссылку в буфер обмена?")
        copy = input("Y/n: ")
        if copy == "Y" or copy == "y" or copy == "Yes" or copy == "yes":
            clearTerm()
            pyperclip.copy(result.get("artwork"))
            print("Скопировано.")
            print("")
            print("Программа будет закрыта через несколько секунд..")
            time.sleep(3)
            quit()
        else:
            clearTerm()
            print("Программа будет закрыта через несколько секунд..")
            time.sleep(3)
            quit()
    else:
        print("Композиция не найдена, проверьте входные данные.")
