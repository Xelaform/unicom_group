from conn2sql import *

#  переменная с именем базы SQL
basename = '[A_TaskManager_LocalList_cd165d4d-e751-4ae1-9313-d83c8a677643_0]'

# обнуляем счётчики
all_row = 0  #  всего строк
processed = 0  #  обработанно
unprocessed = 0  #  необработано
not_ringing = 0  #  недозвон
sale = 0  #  продажа
refusing = 0  #  отказ
call_back = 0  #  перезвонить

headholder, results = base(basename)

#  определяем порядковый номер колонки с именем "Статус"
status = (headholder.index('Статус'))
#  перебираем каждую строку в цикле
for row in results:
    all_row += 1
    #  узнаём сколько всего столбцов
    num_row = len(row)
    #  если в столбце "Статус" нет значения (пусто)
    if row[status] == "":
        #  инкремировать значение переменной unprocessed на 1
        unprocessed += 1
    #  если в столбце "Статус" значение "Занято" или "Не отвечает" или "Автоответчик\Не отвечает"
    elif row[status] == "Занято" or row[status] == "Не отвечает" or row[status] == "Автоответчик\\Не отвечает":
        #  инкремировать значение переменной not_ringing на 1
        not_ringing += 1
    #  если в столбце "Статус" значение "Перезвонить"
    elif row[status] == "Перезвонить":
        #  инкремировать значение переменной call_back на 1
        call_back += 1
    #  если в столбце "Статус" значение "Продажа"
    elif row[status] == "Заявка":
        #  инкремировать значение переменной sale на 1
        sale += 1
    #  если в столбце "Статус" значение "Отказ"
    elif row[status] == "Отказ":
        #  инкремировать значение переменной refusing на 1
        refusing += 1
    else:
        print("Ошибка в строке - ", all_row, row[status])

processed = all_row - unprocessed
contacts_took_place = sale + refusing + call_back

proc_processed = str(round((all_row - unprocessed) / all_row * 100, 2))  #  процент обработаных
proc_unprocessed = str(round(unprocessed / all_row * 100, 2))  #  процент необработаных
proc_not_ringing = str(round(not_ringing / all_row * 100, 2))  #  процент недозвонов
proc_contacts_took_place = str(round((sale + refusing + call_back) / all_row * 100, 2))  #  процент состоявшихся контактов
proc_sale = str(round(sale / all_row * 100, 2))  #  процент продаж
proc_refusing = str(round(refusing / all_row * 100, 2))  #  процент отказов
proc_call_back = str(round(call_back / all_row * 100, 2))  #  процент перезвонов


#print_stat2(all_row, processed, unprocessed, not_ringing, contacts_took_place, sale, refusing, call_back,
#               proc_processed, proc_unprocessed, proc_not_ringing, proc_contacts_took_place,
#               proc_sale, proc_refusing, proc_call_back)

print_stat(all_row, processed, unprocessed, not_ringing, contacts_took_place, sale, refusing, call_back,
               proc_processed, proc_unprocessed, proc_not_ringing, proc_contacts_took_place,
               proc_sale, proc_refusing, proc_call_back)
