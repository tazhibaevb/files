# 1.1 Создайте database.txt файл с несколькими логинами и паролями. Затем попросите пользователя
# войти или зарегистрироваться. Спросите его логин и пароль. Если такой логин уже есть скажите
# ему что логин уже существует и предложите зарегистрироваться спросив пароль.
# Если такого логина неоказалось среди уже существющих продолжайте регистрацию.
# Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.

# my_file = open('datebase.txt', 'w')
# my_file.write('qwerty 12345, ytrewq 54321')
# my_file.close()
#
# my_file = open('datebase.txt', 'r')
# log1 = my_file.read(6)
# my_file.seek(14)
# log2 = my_file.read(6)
# full = my_file.read()
#
# messages = list()
#
# for i in range(1):
#     choice = input('войти - нажмите (v), зарегистрироваться - нажмите (z): ')
#     if choice.lower() == 'v':
#         log = input('введите логин (qwerty): ')
#         password = input('введите пароль (12345): ')
#         if log and password in full:
#             print('вы вошли')
#         else:
#             print('введите правильный логин или пароль: ')
#     elif choice.lower() == 'z':
#         log = input('введите логин: ')
#         if log == log1 or log == log2:
#             password = input(' такой логин уже есть, введите пароль: ')
#             password1 = input('повторите пароль: ')
#             if password == password1:
#                 messages.append(log + "\n")
#                 messages.append(password)
#                 print(messages)
#             else:
#                 print('пароли не совпадают')
#
# my_file.close()