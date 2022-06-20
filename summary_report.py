import csv

summary = {0: 'Необработано',
           1: 'Недозвон',
           2: 'Недозвон',
           3: 'Недозвон',
           4: 'Недозвон',
           5: 'Недозвон',
           6: 'Недозвон',
           7: 'Недозвон',
           8: 'Отказ',
           9: 'Отказ',
           10: 'Отказ',
           11: 'Отказ',
           12: 'Отказ',
           13: 'Отказ',
           14: 'Отказ',
           15: 'Отказ',
           16: 'Отказ',
           17: 'Отказ',
           18: 'Отказ',
           19: 'Отказ',
           20: 'Перезвонить',
           21: 'Отказ',
           22: 'Отказ',
           23: 'Отказ',
           24: 'Отказ',
           25: 'Отказ',
           26: 'Отказ',
           27: 'Отказ',
           28: 'Недозвон',
           29: 'Недозвон',
           30: 'Недозвон',
           31: 'Продажа',
           32: 'Продажа',
           33: 'Продажа',
           34: 'Продажа',
           35: 'Продажа',
           36: 'Недозвон',
           37: 'Недозвон',
           38: 'Недозвон',
           39: 'Отказ',
           40: 'Продажа',
           41: 'Отказ',
           42: 'Отказ'}
title = {0: 'Id',
         1: 'base',
         2: 'uniq_number_id',
         3: 'client_id',
         4: 'phone',
         5: 'CallResultID'}

unprocessed = 0 # необработано
refusing = 0 # отказ
call_back = 0 # перезвонить
not_ringing = 0 # недозвон
sale = 0 # продажа
all_collumn = 0

# открываем файл для чтения и присваеваем переменной csv_file
with open('apr_mimo_minimum_0104.csv', 'r', newline='', encoding="UTF-8") as csv_file:
    # используя функцию csv.reader считываем содержимое файла (используем разделитель ";")
    text = csv.reader(csv_file, delimiter=';')
    # перебираем каждую строку в цикле
    next(text, None)
    for row in text:
        all_collumn += 1
        # узнаём сколько всего столбцов
        num_row = len(row)
        # если в последнем столбце нет значения
        if row[num_row - 1] == "":
            # инкремировать значение переменной unprocessed на 1
            unprocessed += 1
        # если в последнем столбце значение = 1-7 или 28-30 или 36-38
        elif row[num_row - 1] == "1" or row[num_row - 1] == "2" or row[num_row - 1] == "3" or row[num_row - 1] == "4" or row[num_row - 1] == "5" or row[num_row - 1] == "6" or row[num_row - 1] == "7" or row[num_row - 1] == "28" or row[num_row - 1] == "29" or row[num_row - 1] == "30" or row[num_row - 1] == "36" or row[num_row - 1] == "37" or row[num_row - 1] == "38":
            # инкремировать значение переменной not_ringing на 1
            not_ringing += 1
        # если в последнем столбце значение = 20
        elif row[num_row - 1] == "20":
            # инкремировать значение переменной call_back на 1
            call_back += 1
        # если в последнем столбце значение =  31-35 и 40
        elif row[num_row - 1] == "31" or row[num_row - 1] == "32" or row[num_row - 1] == "33" or row[num_row - 1] == "34" or row[num_row - 1] == "35" or row[num_row - 1] == "40":
            # инкремировать значение переменной sale на 1
            sale += 1
        # если в последнем столбце значение = 8-19 и 21-27 и 39 и 41-42
        elif row[num_row - 1] == "8" or row[num_row - 1] == "9" or row[num_row - 1] == "10" or row[num_row - 1] == "11" or row[num_row - 1] == "12" or row[num_row - 1] == "13" or row[num_row - 1] == "14" or row[num_row - 1] == "15" or row[num_row - 1] == "16" or row[num_row - 1] == "17" or row[num_row - 1] == "18" or row[num_row - 1] == "19" or row[num_row - 1] == "21" or row[num_row - 1] == "22" or row[num_row - 1] == "23" or row[num_row - 1] == "24" or row[num_row - 1] == "25" or row[num_row - 1] == "26" or row[num_row - 1] == "27" or row[num_row - 1] == "39" or row[num_row - 1] == "41" or row[num_row - 1] == "42":
            # инкремировать значение переменной refusing на 1
            refusing += 1
        else:
            print("Ошибка в строке - ", all_collumn, row[num_row - 1])

    print("Всего ЛС - ", all_collumn, " (100%)", sep="")
    print("необработано - ", unprocessed, " (", round(unprocessed / all_collumn * 100, 2), "%)", sep="")
    print("отказ - ", refusing, " (", round(refusing / all_collumn * 100, 2), "%)", sep="")
    print("перезвонить - ", call_back, " (", round(call_back / all_collumn * 100, 2), "%)", sep="")
    print("недозвон - ", not_ringing, " (", round(not_ringing / all_collumn * 100, 2), "%)", sep="")
    print("продажа - ", sale, " (", round(sale / all_collumn * 100, 2), "%)", sep="")
