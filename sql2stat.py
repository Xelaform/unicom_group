import pyodbc
import csv
import tkinter

driver = "ODBC Driver 17 for SQL Server"
server = "192.168.88.100"
database = "oktell"
uid = "AutelService2"
password = "3QAm5eLm4cH3"


def read_sql_table(records):
    try:
        conn = pyodbc.connect('DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (driver, server, database, uid, password))
        cursor = conn.cursor()

        # Получаем выборку всех баз Мая сортированных по колонке JoinedTable в алфавитном порядке
        cursor.execute("SELECT Name, JoinedTable FROM oktell_settings.dbo.A_TaskManager_Lists WHERE JoinedTable LIKE '%s' ORDER BY JoinedTable" % (records))

        result = cursor.fetchall()
        #column_names = [column[0] for column in cursor.description]
        with open("C:/1234/database_list.csv", mode="w", newline="") as w_file:
            c = csv.writer(w_file, delimiter=";")
            c.writerows(result)
        print("\n", "Файл успешно создан")
        conn.close()

    except conn.Error as error:
        print("Ошибка при работе с SQL", error)

tkinter._test()

answer1 = int(input("ЦТМ[1] или АПСЕЙЛ[2]: "))
if answer1 == 1:
    base_name = "may_ctm"
    print("Ты выбрал ЦТМ")
elif answer1 == 2:
    base_name = "may_upsale"
    print("Ты выбрал АПСЕЙЛ")

answer2 = int(input("ВОЛГА[1], ДВ[2], МиМО[3], СЗФО[4], СИБИРЬ[5], УРАЛ[6], ЦЕНТР[7], ЮГ[8] или ВСЕ[0]: "))
if answer2 == 0:
    mrf_name = "%"
    print("Ты выбрал ВСЕ")
elif answer2 == 1:
    mrf_name = "_volga%"
    print("Ты выбрал ВОЛГА")
elif answer2 == 2:
    mrf_name = "_dv%"
    print("Ты выбрал ДВ")
elif answer2 == 3:
    mrf_name = "_mimo%"
    print("Ты выбрал МиМО")
elif answer2 == 4:
    mrf_name = "_szfo%"
    print("Ты выбрал СЗФО")
elif answer2 == 5:
    mrf_name = "_siberia%"
    print("Ты выбрал СИБИРЬ")
elif answer2 == 6:
    mrf_name = "_ural%"
    print("Ты выбрал УРАЛ")
elif answer2 == 7:
    mrf_name = "_center%"
    print("Ты выбрал ЦЕНТР")
elif answer2 == 8:
    mrf_name = "_south%"
    print("Ты выбрал ЮГ")

read_sql_table(base_name+mrf_name)