import pyodbc
import csv
#from prettytable import PrettyTable
# oktell_settings.dbo.A_Users

# обнуляем счётчики
unprocessed = 0 # необработано
refusing = 0 # отказ
call_back = 0 # перезвонить
not_ringing = 0 # недозвон
sale = 0 # продажа
all_row = 0 # всего строк

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=192.168.88.100; DATABASE=oktell; UID=AutelService2; PWD=3QAm5eLm4cH3")
cursor = conn.cursor()

# Получаем выборку из таблицы ВетЭксперт
cursor.execute("SELECT * FROM [A_TaskManager_LocalList_cd165d4d-e751-4ae1-9313-d83c8a677643_0]")
fieldnames = [column[0] for column in cursor.description]
result = cursor.fetchall()
# Заголовки таблицы
#fieldnames = ['Id', 'Телефон', 'Телефон2', 'Оператор', 'Статус', 'Дубль', 'calldate', 'effortcount', 'chainid', 'length', 'Питомец', 'ФИО']

with open("C:/1234/5678.csv", mode="w", encoding='utf8', newline='') as w_file:
    c = csv.writer(w_file, delimiter=";")
    c.writerow(fieldnames)
    for row in result:
        c.writerow(row)
print("Файл создан успешно")
print("-------------------")
conn.close()


# открываем файл для чтения и присваеваем переменной csv_file
with open('C:/1234/5678.csv', 'r', newline='', encoding="UTF-8") as csv_file:
    # используя функцию csv.DictReader считываем содержимое файла (используем разделитель ";")
    text = csv.DictReader(csv_file, delimiter=';', fieldnames=fieldnames)
    # пропускаем первую строку с заголовком
    next(text, None)
    # перебираем каждую строку в цикле
    for row in text:
        all_row += 1
        # узнаём сколько всего столбцов
        num_row = len(row)
        # если в столбце CallResultID нет значения
        if row['Статус'] == "" or row['Статус'] == "0":
            # инкремировать значение переменной unprocessed на 1
            unprocessed += 1
        # если в столбце CallResultID значение = 1-7 или 28-30 или 36-38
        elif row['Статус'] == "Занято" or row['Статус'] == "Не отвечает" or row['Статус'] == "Автоответчик\Не отвечает":
            # инкремировать значение переменной not_ringing на 1
            not_ringing += 1
        # если в столбце CallResultID значение = 20
        elif row['Статус'] == "Перезвонить":
            # инкремировать значение переменной call_back на 1
            call_back += 1
        # если в столбце CallResultID значение Продажа
        elif row['Статус'] == "Заявка":
            # инкремировать значение переменной sale на 1
            sale += 1
        # если в столбце CallResultID значение = Отказ
        elif row['Статус'] == "Отказ":
            # инкремировать значение переменной refusing на 1
            refusing += 1
        else:
            print("Ошибка в строке - ", all_row, row['Статус'])

    print("Всего ЛС - ", all_row, " (100%)", sep="")
    print("Обработано - ", all_row - unprocessed, " (", round((all_row - unprocessed) / all_row * 100, 2), "%)", sep="")
    print("Необработано - ", unprocessed, " (", round(unprocessed / all_row * 100, 2), "%)", sep="")
    print("Недозвон - ", not_ringing, " (", round(not_ringing / all_row * 100, 2), "%)", sep="")
    print("Состоялось контактов - ", sale + refusing + call_back, " (", round((sale + refusing + call_back) / all_row * 100, 2), "%)", sep="")
    print("Продажа - ", sale, " (", round(sale / all_row * 100, 2), "%)", sep="")
    print("Отказ - ", refusing, " (", round(refusing / all_row * 100, 2), "%)", sep="")
    print("Перезвонить - ", call_back, " (", round(call_back / all_row * 100, 2), "%)", sep="")
