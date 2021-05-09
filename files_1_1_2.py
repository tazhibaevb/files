# 1.1.2 Возьмите текст #2 и вставьте его в текстовый файл.
# Возьмите данные из файла и сложите зарплату за Май, Июль, Сентябрь и Ноябрь и посчитайте
# среднее арифмитечское за эти месяца.

# import shelve
# FILENAME = "zp.txt"
# with shelve.open(FILENAME) as zp:
#     zp["January"] = 18000
#     zp["February"] = 32641
#     zp["March"] = 28300
#     zp["April"] = 11200
#     zp["May"] = 21100
#     zp["June"] = 19000
#     zp["July"] = 8000
#     zp["August"] = 72000
#     zp["September"] = 12300
#     zp["October"] = 17000
#     zp["November"] = 25000
#     zp["December"] = 30000
#
# with shelve.open(FILENAME) as zp:
#     print((zp["May"]+zp["July"]+zp["September"]+zp["November"])/4)