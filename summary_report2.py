import csv
#from prettytable import PrettyTable

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

# обнуляем счётчики
unprocessed = 0 # необработано
refusing = 0 # отказ
call_back = 0 # перезвонить
not_ringing = 0 # недозвон
sale = 0 # продажа
all_row = 0 # всего строк

# открываем файл для чтения и присваеваем переменной csv_file
with open('C:/1234/S1234.csv', 'r', newline='', encoding="UTF-8") as csv_file:
    # используя функцию csv.DictReader считываем содержимое файла (используем разделитель ";")
    text = csv.DictReader(csv_file, delimiter=';')
    # пропускаем первую строку с заголовком
    # next(text, None)
    # перебираем каждую строку в цикле
    for row in text:
        all_row += 1
        # узнаём сколько всего столбцов
        num_row = len(row)
        # если в столбце CallResultID нет значения
        if row['CallResultID'] == "" or row['CallResultID'] == "0":
            # инкремировать значение переменной unprocessed на 1
            unprocessed += 1
        # если в столбце CallResultID значение = 1-7 или 28-30 или 36-38
        elif row['CallResultID'] == "1" or row['CallResultID'] == "2" or row['CallResultID'] == "3" or row['CallResultID'] == "4" or row['CallResultID'] == "5" or row['CallResultID'] == "6" or row['CallResultID'] == "7" or row['CallResultID'] == "28" or row['CallResultID'] == "29" or row['CallResultID'] == "30" or row['CallResultID'] == "36" or row['CallResultID'] == "37" or row['CallResultID'] == "38":
            # инкремировать значение переменной not_ringing на 1
            not_ringing += 1
        # если в столбце CallResultID значение = 20
        elif row['CallResultID'] == "20":
            # инкремировать значение переменной call_back на 1
            call_back += 1
        # если в столбце CallResultID значение =  31-35 и 40
        elif row['CallResultID'] == "31" or row['CallResultID'] == "32" or row['CallResultID'] == "33" or row['CallResultID'] == "34" or row['CallResultID'] == "35" or row['CallResultID'] == "40":
            # инкремировать значение переменной sale на 1
            sale += 1
        # если в столбце CallResultID значение = 8-19 и 21-27 и 39 и 41-42
        elif row['CallResultID'] == "8" or row['CallResultID'] == "9" or row['CallResultID'] == "10" or row['CallResultID'] == "11" or row['CallResultID'] == "12" or row['CallResultID'] == "13" or row['CallResultID'] == "14" or row['CallResultID'] == "15" or row['CallResultID'] == "16" or row['CallResultID'] == "17" or row['CallResultID'] == "18" or row['CallResultID'] == "19" or row['CallResultID'] == "21" or row['CallResultID'] == "22" or row['CallResultID'] == "23" or row['CallResultID'] == "24" or row['CallResultID'] == "25" or row['CallResultID'] == "26" or row['CallResultID'] == "27" or row['CallResultID'] == "39" or row['CallResultID'] == "41" or row['CallResultID'] == "42":
            # инкремировать значение переменной refusing на 1
            refusing += 1
        else:
            print("Ошибка в строке - ", all_row, row['CallResultID'])

    print("Всего ЛС - ", all_row, " (100%)", sep="")
    print("обработано - ", all_row - unprocessed, " (", round((all_row - unprocessed) / all_row * 100, 2), "%)", sep="")
    print("необработано - ", unprocessed, " (", round(unprocessed / all_row * 100, 2), "%)", sep="")
    print("недозвон - ", not_ringing, " (", round(not_ringing / all_row * 100, 2), "%)", sep="")
    print("состоялось контактов - ", sale + refusing + call_back, " (", round((sale + refusing + call_back) / all_row * 100, 2), "%)", sep="")
    print("продажа - ", sale, " (", round(sale / all_row * 100, 2), "%)", sep="")
    print("отказ - ", refusing, " (", round(refusing / all_row * 100, 2), "%)", sep="")
    print("перезвонить - ", call_back, " (", round(call_back / all_row * 100, 2), "%)", sep="")
