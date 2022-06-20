import pyodbc
import csv


driver = "ODBC Driver 17 for SQL Server"
server = "192.168.88.100"
database = "oktell"
uid = "AutelService2"
password = "3QAm5eLm4cH3"

# oktell_settings.dbo.A_Users


conn = pyodbc.connect('DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (driver, server, database, uid, password))
#conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=192.168.88.100; DATABASE=oktell; UID=AutelService2; PWD=3QAm5eLm4cH3")
cursor = conn.cursor()

# Получаем выборку всех баз Мая сортированных по колонке JoinedTable в алфавитном порядке
#cursor.execute("SELECT Name, JoinedTable FROM oktell_settings.dbo.A_TaskManager_Lists WHERE JoinedTable LIKE 'may%' ORDER BY JoinedTable")
cursor.execute("SELECT Name, JoinedTable FROM oktell_settings.dbo.A_TaskManager_Lists WHERE JoinedTable LIKE 'may_upsale%' ORDER BY JoinedTable")
cursor.execute("SELECT * FROM may_upsale_siberia_warranty_0205")

result = cursor.fetchall()
column_names = [column[0] for column in cursor.description]
with open("C:/1234/5678.csv", mode="w", newline="") as w_file:
        c = csv.writer(w_file, delimiter=";")
        c.writerows(result)
print("Файл создан успешно")
conn.close()