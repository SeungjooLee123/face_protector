import pymysql

def create(tableName):

    connection = pymysql.connect(
                    host = '127.0.0.1',
                    database = 'chosun',
                    user = 'root',
                    password = 'a5214645'
            )

    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE "+ tableName +" (name VARCHAR(255), img MEDIUMTEXT, size VARCHAR(255))")

    finally:
        connection.commit()
        connection.close()
