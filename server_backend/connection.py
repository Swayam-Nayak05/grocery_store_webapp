import mysql.connector
  
__el=None
def get_sql_connection():
    global __el
    if __el is None:
        __el= el=mysql.connector.connect(user='root',password='Swayam@9876',database='grocery_store')

    return __el
