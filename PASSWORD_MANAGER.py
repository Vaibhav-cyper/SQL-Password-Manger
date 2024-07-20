import string
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your SQL Password",
    database="Your Database Name"
)


global cursor

cursor = mydb.cursor()


class password_manager:

    #table_id = 0

    def __init__(self, table_name):

        self.table_name = table_name
        self.desc_tables = desc_tables

        #store_id =password_manager.table_id +1

    def create_table(table_name):
        try:
            sql = (
                f"CREATE TABLE {table_name}(Name VARCHAR(255), Account VARCHAR(255), Username VARCHAR(255), Password VARCHAR(255))"
            )
            cursor.execute(sql)

            cursor.execute("SHOW TABLES")

            for x in cursor:
                if t_name in cursor:
                    print(name, " record created")
            print("\n", t_name, "record created")

        except mysql.connector.errors.ProgrammingError:
            print("\n", "Table Already Existed !!")

    def Open_records():
        cursor.execute(f"SELECT * FROM {self.name}")
        myresult = cursor.fetchall()
        for x in myresult:
            print("Record details :~")
            print(x)  # it open the record

        ''' We use the fetchall() method, which fetches all rows from the last executed statement.'''

    def desc_tables(table_name):
        cursor.execute(f"DESC {table_name}")
        result = cursor.fetchall()
        for x in result:
            print(x)


if mydb.is_connected():
    print("Enter Your Choice :")
    print("1 . Show Records ")
    print("2 . Create Record ")
    print("3 . Open Record structure ")
    print("4 . Insert  in Record")
    print("5 . Open Record Detail")
    print("6 . Delete Record ")
    
    ch = int(input("Enter Your Choice :"))

    def show_tables():
        cursor.execute("SHOW TABLES")
        print("Diplaying Records :~")
        for x in cursor:
            print("\n", "Records are :~ ", x)  # it print the tables name

t_name = input("Enter Record Name :")
if ch == 1:
    show_tables()

if ch == 2:
    password_manager.create_table(t_name)

    #  to print the record is created
    cursor.execute("SHOW TABLES")
    for x in cursor:
        if t_name in cursor:
            print(f"your {t_name} created")
        print(t_name, "record created")


if ch == 3:
    DESC_table = input("Enter the name to see the structure :")
    password_manager.desc_tables(DESC_table)
if ch == 4:
    INSERT_table = input("Enter the record name :")
    NAME = input('Enter The Name :')
    ACCOUNT = input('Enter The Account :')
    USERNAME = input('Enter The UserName :')
    PASSWORD = input('Enter The Password :')

    def insert(NAME, ACCOUNT, USERNAME, PASSWORD, ):

        
        sql = (f"INSERT INTO {INSERT_table}(name , account , username , password ) VALUES(%s,%s,%s,%s)")

        val = ((NAME, ACCOUNT, USERNAME, PASSWORD))

        cursor.execute(sql, val)
        mydb.commit()
        print("/n", cursor.rowcount, "record inserted")
            
    insert(NAME, ACCOUNT, USERNAME, PASSWORD)
if ch == 5:
    cursor.execute(f"SELECT * FROM {t_name}")
    result = cursor.fetchall()
    for x in result:
        print(x)
    
if ch == 6:
    def Delete_records():
        show_tables()
        dt_name = input("enter the table name you want to delete :")
        sql = (f"DROP TABLE IF EXISTS {dt_name}")
        cursor.execute(sql)

        # to delete the record
        cursor.execute("SHOW TABLES")
        for x in cursor:
            if dt_name not in cursor:
                print("\n", dt_name, "record deleted")

    Delete_records()

