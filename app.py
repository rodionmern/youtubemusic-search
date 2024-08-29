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

inputChoice = input("")
clearTerm()

query = input("Введи автора и название композиции: ")
result = YouTubeMusicAPI.search(query)

if inputChoice == "0":
    clearTerm()
    if result:
        print(f'Исполнитель: {result.get("name")}\nНазвание композиции: {result.get("title")}\nURL адрес: {result.get("url")}\n')
        print('Скопировать ссылку в буфер обмена?')
        copy = input("Y/n: ")
        if copy == "Y" or copy == "y" or copy == "Yes" or copy == "yes":
            clearTerm()
            pyperclip.copy(result.get("url"))
            print('Скопировано.\nПрограмма будет закрыта через несколько секунд..')
            time.sleep(3)
            quit()
        else:
            clearTerm()
            print('Программа будет закрыта через несколько секунд..')
            time.sleep(3)
            quit()
    else:
        print("Композиция не найдена, проверьте входные данные.")
elif inputChoice == "1":
    clearTerm()
    if result:
        print(f'Исполнитель: {result.get("name")}\nНазвание композиции: {result.get("title")}\nОбложка: {result.get("artwork")}\n')
        print('Скопировать ссылку в буфер обмена?')
        copy = input("Y/n: ")
        if copy == "Y" or copy == "y" or copy == "Yes" or copy == "yes":
            clearTerm()
            pyperclip.copy(result.get("artwork"))
            print('Скопировано.\nПрограмма будет закрыта через несколько секунд..')
            time.sleep(3)
            quit()
        else:
            clearTerm()
            print('Программа будет закрыта через несколько секунд..')
            time.sleep(3)
            quit()
    else:
        print('Композиция не найдена, проверьте входные данные.')
