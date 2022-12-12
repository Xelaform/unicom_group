from tkinter import *
import pyodbc


driver = "ODBC Driver 17 for SQL Server"
server = "192.168.88.100"
database = "oktell"
uid = "AutelService2"
password = "3QAm5eLm4cH3"

#  oktell_settings.dbo.A_Users


def base():
    conn = pyodbc.connect('DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (driver, server, database, uid, password))
    cursor = conn.cursor()
    #cursor.execute('SELECT * FROM %s' % basename)
    # Получаем выборку всех баз Мая сортированных по колонке JoinedTable в алфавитном порядке
    cursor.execute("SELECT Name, JoinedTable FROM oktell_settings.dbo.A_TaskManager_Lists WHERE JoinedTable LIKE 'dec_upsale%' ORDER BY JoinedTable")
    fieldnames = [column[0] for column in cursor.description]
    table = cursor.fetchall()
    conn.close()
    return table

#root = Tk()
#var1 = StringVar()
#root.title("Статистика \"Юником\"")
#root.geometry("800x200")
#table = base()
#var1.set(table)
#Label(root, textvariable=var1).pack(side=LEFT)

root=Tk()
root.title("Статистика \"Юником\"")
root.geometry("800x600")
Label(root,text="Список баз:").place(x=5,y=0)
placement=20
table = base()
for tasks in table:
    Checkbutton(root,text=str(tasks)).place(x=5,y=placement)
    placement+=20

root.mainloop()