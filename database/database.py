import mysql.connector
from mysql.connector import Error

def get_attack_data():
    """
    Retrieves attack data from the database for analysis.
    """
    try:
        connection = mysql.connector.connect(host='localhost',
                                              database='honeypot_db',
                                              user='user',
                                              password='password')

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM attacks")
            result = cursor.fetchall()
            return result

    except Error as e:
        print(f"Error while connecting to database: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
