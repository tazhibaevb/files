# 1.1.1 Напишите программу которая спрашивает от пользователя 2 вещи:
# 1.Путь до картинки которую нужно изменить.
# 2.Путь до картинки НА которую нужно изменить.
# Если оба пути существуют перепишите первую картинку на вторую,
# если нет скажите пользователю какой картинке не существует.
#
# import pickle
#
# put1 = 'C:/Users/99655/Downloads/photo/cat.jpg'
# put2 = 'C:/Users/99655/Downloads/photo/zak.jpg'
# pic1 = input('путь до первой картинки: ')
# pic2 = input('путь до второй картинки: ')
# cat ='C:/Users/99655/Downloads/photo/cat.jpg'
# zak ='C:/Users/99655/Downloads/photo/zak.jpg'
# if pic1 == put1 and pic2 == put2:
#     with open(cat, 'wb') as file:
#         pickle.dump('C:/Users/99655/Downloads/photo/zak.jpg', cat)
#
#     with open(cat, 'rb') as file1:
#         a = pickle.load(file1)
#         print(a)