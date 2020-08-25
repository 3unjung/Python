import mysql.connector

if __name__ == '__main__':
    try:
        sqlConnection = mysql.connector.connect(

            host="localhost",
            user="root",
            password="",
            database="arcenciel"
        )

        cursor = sqlConnection.cursor()
        cursor.execute("ALTER TABLE test ADD squery int(13);")

    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))


