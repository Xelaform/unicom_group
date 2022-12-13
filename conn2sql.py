import pyodbc
from prettytable import PrettyTable

driver = "ODBC Driver 17 for SQL Server"
server = "192.168.88.100"
database = "oktell"
uid = "AutelService2"
password = "3QAm5eLm4cH3"

#  oktell_settings.dbo.A_Users


def base(basename):
    conn = pyodbc.connect('DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (driver, server, database, uid, password))
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM %s' % basename)
    fieldnames = [column[0] for column in cursor.description]
    table = cursor.fetchall()
    print("Подключение к SQL серверу успешно")
    # print("---------------------------------")
    conn.close()
    return fieldnames, table

def get_stat(row, status, all_row, unprocessed, not_ringing, sale, refusing, call_back):
    # если в столбце CallResultID нет значения
    if row[status] == None or row[status] == 0:
        # инкремировать значение переменной unprocessed на 1
        unprocessed += 1
    # если в столбце CallResultID значение = 1-7 или 28-30 или 36-38
    elif row[status] == 1 or row[status] == 2 or row[status] == 3 or row[
        status] == 4 or row[status] == 5 or row[status] == 6 or row[
        status] == 7 or row[status] == 28 or row[status] == 29 or row[
        status] == 30 or row[status] == 36 or row[status] == 37 or row[
        status] == 38:
        # инкремировать значение переменной not_ringing на 1
        not_ringing += 1
    # если в столбце CallResultID значение = 20
    elif row[status] == 20:
        # инкремировать значение переменной call_back на 1
        call_back += 1
    # если в столбце CallResultID значение =  31-35 и 40
    elif row[status] == 31 or row[status] == 32 or row[status] == 33 or row[
        status] == 34 or row[status] == 35 or row[status] == 40:
        # инкремировать значение переменной sale на 1
        sale += 1
    # если в столбце CallResultID значение = 8-19 и 21-27 и 39 и 41-42
    elif row[status] == 8 or row[status] == 9 or row[status] == 10 or row[
        status] == 11 or row[status] == 12 or row[status] == 13 or row[
        status] == 14 or row[status] == 15 or row[status] == 16 or row[
        status] == 17 or row[status] == 18 or row[status] == 19 or row[
        status] == 21 or row[status] == 22 or row[status] == 23 or row[
        status] == 24 or row[status] == 25 or row[status] == 26 or row[
        status] == 27 or row[status] == 39 or row[status] == 41 or row[
        status] == 42:
        # инкремировать значение переменной refusing на 1
        refusing += 1
    else:
        print("Ошибка в строке - ", all_row, row[status])
    processed = all_row - unprocessed
    contacts_took_place = sale + refusing + call_back
    proc_processed = str(round((all_row - unprocessed) / all_row * 100, 2))  # процент обработаных
    proc_unprocessed = str(round(unprocessed / all_row * 100, 2))  # процент необработаных
    proc_not_ringing = str(round(not_ringing / all_row * 100, 2))  # процент недозвонов
    proc_contacts_took_place = str(round((sale + refusing + call_back) / all_row * 100, 2))  # процент сост. контактов
    proc_sale = str(round(sale / all_row * 100, 2))  # процент продаж
    proc_refusing = str(round(refusing / all_row * 100, 2))  # процент отказов
    proc_call_back = str(round(call_back / all_row * 100, 2))  # процент перезвонов
    return all_row, processed, unprocessed, not_ringing, contacts_took_place, sale, refusing, call_back, \
           proc_processed, proc_unprocessed, proc_not_ringing, proc_contacts_took_place, proc_sale, proc_refusing, \
           proc_call_back


def print_stat(all_row, processed, unprocessed, not_ringing, contacts_took_place, sale, refusing, call_back,
               proc_processed, proc_unprocessed, proc_not_ringing, proc_contacts_took_place,
               proc_sale, proc_refusing, proc_call_back):
    mytable = PrettyTable()
    # имена полей таблицы
    mytable.field_names = ["Всего ЛС", "Обработано", "Необработано", "Недозвон", "Сост. контактов", "Продажа", "Отказ",
                           "Перезвонить"]
    # добавление данных по одной строке за раз
    mytable.add_row([all_row, processed, unprocessed, not_ringing, contacts_took_place, sale, refusing, call_back])
    mytable.add_row(["100%", proc_processed + "%", proc_unprocessed + "%", proc_not_ringing + "%",
                     proc_contacts_took_place + "%", proc_sale + "%", proc_refusing + "%", proc_call_back + "%"])
    # вывод таблицы в терминал
    print(mytable)
    return

def print_stat2(all_row, processed, unprocessed, not_ringing, contacts_took_place, sale, refusing, call_back,
                proc_processed, proc_unprocessed, proc_not_ringing, proc_contacts_took_place,
                proc_sale, proc_refusing, proc_call_back):
    print("Всего ЛС - ", all_row, " (100%)", sep="")
    print("обработано - ", processed, " (", proc_processed, "%)", sep="")
    print("необработано - ", unprocessed, " (", proc_unprocessed, "%)", sep="")
    print("недозвон - ", not_ringing, " (", proc_not_ringing, "%)", sep="")
    print("состоялось контактов - ", contacts_took_place, " (", proc_contacts_took_place, "%)", sep="")
    print("продажа - ", sale, " (", proc_sale, "%)", sep="")
    print("отказ - ", refusing, " (", proc_refusing, "%)", sep="")
    print("перезвонить - ", call_back, " (", proc_call_back, "%)", sep="")
    return