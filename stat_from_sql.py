import pyodbc
import csv

ans1 = int(input("ЦТМ[1] или АПСЕЙЛ[2]: "))
base_name = "may_ctm%"

if ans1 == 1:
    print("Ты выбрал ЦТМ")
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server}; SERVER=192.168.88.100; DATABASE=oktell; UID=AutelService2; PWD=3QAm5eLm4cH3")
    cursor = conn.cursor()

    # Получаем выборку всех баз Мая сортированных по колонке JoinedTable в алфавитном порядке
    cursor.execute(r"SELECT Name, JoinedTable FROM oktell_settings.dbo.A_TaskManager_Lists WHERE JoinedTable LIKE (base_name) ORDER BY JoinedTable")

    result = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    with open("C:/1234/database_list.csv", mode="w", newline="") as w_file:
        c = csv.writer(w_file, delimiter=";")
        c.writerows(result)
    print("Файл создан успешно")
elif ans1 == 2:
    print("Ты выбрал АПСЕЙЛ")
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server}; SERVER=192.168.88.100; DATABASE=oktell; UID=AutelService2; PWD=3QAm5eLm4cH3")
    cursor = conn.cursor()

    # Получаем выборку всех баз Мая сортированных по колонке JoinedTable в алфавитном порядке
    cursor.execute(
        "SELECT Name, JoinedTable FROM oktell_settings.dbo.A_TaskManager_Lists WHERE JoinedTable LIKE 'may_upsale%' ORDER BY JoinedTable")

    result = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    with open("C:/1234/database_list.csv", mode="w", newline="") as w_file:
        c = csv.writer(w_file, delimiter=";")
        c.writerows(result)
    print("Файл создан успешно")

conn.close()



# открываем файл для чтения и присваеваем переменной csv_file
with open('C:/1234/database_list.csv', 'r', newline='') as base_list_file:
    # используя функцию csv.DictReader считываем содержимое файла (используем разделитель ";")
    reader = csv.reader(base_list_file, delimiter=';')
    print("Выбири по какой базе нужна статистика")
    for row in reader:
        print(row[0])


